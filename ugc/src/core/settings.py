import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY = os.getenv("SECRET_KEY", "top_secret")
    kafka_host = os.getenv('KAFKA_HOST', 'localhost')
    kafka_port = os.getenv('KAFKA_PORT', '9092')
    jwt_secret_key = os.getenv('JWT_SECRET_KEY', 'top_secret')

    class Config:
        env_file = ".env"