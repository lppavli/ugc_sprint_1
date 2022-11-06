from http import HTTPStatus

from typing import Optional
import uvicorn as uvicorn
from fastapi import FastAPI, Depends, HTTPException
from aiokafka import AIOKafkaProducer
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


from models.progress_film import ProgressFilmModel
from services.auth import Auth
from core.settings import Settings


app = FastAPI(
    title='API for posting user-generated content events to UGC db',
    docs_url="/ugc/openapi",
    openapi_url='/ugc/openapi.json',
    description='',
    version="1.0.0",
)
security = HTTPBearer()
auth_handler = Auth()
aio_producer: Optional[AIOKafkaProducer] = None
settings = Settings()


@app.on_event("startup")
async def startup():
    global aio_producer
    aio_producer = AIOKafkaProducer(
        **{
            'bootstrap_servers': '{}:{}'.format(
                settings.kafka_host,
                settings.kafka_port
            )
        }
                                    )
    await aio_producer.start()


@app.on_event("shutdown")
async def shutdown():
    await aio_producer.stop()


@app.post('/progress_film/', tags=["progress film"])
async def post_event(
    progress_film: ProgressFilmModel,
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    token = credentials.credentials
    user_id = auth_handler.decode_token(token)
    try:
        await aio_producer.send(
            topic='views',
            value=progress_film.json().encode(),
            key=f"{user_id}+{progress_film.movie_id}".encode(),
        )
        return {'msg': 'ok'}
    except Exception as e:
        raise HTTPException(status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
                            detail=e.args[0].str())


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8001,
    )