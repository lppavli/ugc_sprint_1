import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    kafka_host = os.getenv('KAFKA_HOST', 'localhost')
    kafka_port = os.getenv('KAFKA_PORT', 9092)
    kafka_topic = os.getenv('KAFKA_TOPIC', 'views')
    clickhouse_host = os.getenv('CLICKLHOUSE_HOST', 'localhost')
    clickhouse_port = os.getenv('CLICKLHOUSE_PORT', 9000)
    messages_count = os.getenv('MESSAGES_COUNT', 1)
    project_name = os.getenv('PROJECT_NAME', 'api kafka')
    KAFKA_INSTANCE = f"{kafka_host}:{kafka_port}"
    class Config:
        env_file = ".env"


settings = Settings()
print(settings)