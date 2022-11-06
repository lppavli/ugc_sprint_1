FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#RUN apk update && \
#    apk add build-base librdkafka-dev && \
#    apk --no-cache add curl && \
#    pip install --upgrade pip && \

COPY . .
#EXPOSE 8001
RUN python -m pip install -r requirements.txt
#ENTRYPOINT python -m main
#CMD gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8001
CMD uvicorn main:app --host 0.0.0.0 --port 8001