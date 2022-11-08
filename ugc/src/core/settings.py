from pydantic import BaseSettings


class Settings(BaseSettings):
    kafka_host: str = 'localhost'
    kafka_port: int = 9092
    jwt_secret_key: str = 'top_secret'

    class Config:
        env_file = ".env"