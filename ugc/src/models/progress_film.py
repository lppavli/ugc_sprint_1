from datetime import datetime

from pydantic import UUID4, BaseModel


class ProgressFilmModel(BaseModel):
    movie_id: UUID4
    viewing_progress: int