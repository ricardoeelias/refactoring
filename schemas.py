from datetime import date

from pydantic import BaseModel, Field


class Movie(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=3, max_length=50)
    overview: str = Field(min_length=10, max_length=150)
    release: date = Field(
        default=date.today(),
        ge=date(1970, 1, 1),
        le=date.today(),
    )
    rating: float = Field(default=0.0, ge=0.0, le=10.0)
    category: str = Field(
        pattern=r"^(Comedia|Acción|Ficción|Romance|Aventura|Infantil|Drama|Terror|Biográfica|Musical)$"
    )
    earnings: float = Field(default=0.0, ge=0.0)
