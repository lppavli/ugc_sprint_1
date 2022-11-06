from aiokafka import AIOKafkaProducer

from src.api.v1.event_schema import EventCreate


class EventService:
    def __init__(self, producer: AIOKafkaProducer):
        self.producer = producer

    async def post_event(self) -> str:
        await self.producer.send_and_wait(
            topic='views',
            value=b'1611039931',
            key=b'500271+tt0120338',
        )
        return 'OK'