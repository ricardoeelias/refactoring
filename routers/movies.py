from typing import Any

from fastapi import APIRouter, HTTPException, Request

from schemas import Movie


router = APIRouter(prefix="/movies", tags=["Movies"])


def _movies(request: Request) -> list[dict[str, Any]]:
    return request.app.state.movies


@router.get("/", response_model=list[Movie])
def get_movies(request: Request, category: str | None = None) -> list[dict[str, Any]]:
    movies = _movies(request)
    if category is None:
        return movies
    return [movie for movie in movies if movie["category"] == category]


@router.get("/{movie_id}", response_model=Movie)
def get_movie(movie_id: int, request: Request) -> dict[str, Any]:
    movie = next(
        (movie for movie in _movies(request) if movie["id"] == movie_id),
        None,
    )
    if movie is None:
        raise HTTPException(
            status_code=404,
            detail=f"Película con id = {movie_id} no encontrada",
        )
    return movie


@router.post("/", response_model=list[Movie])
def create_movie(movie: Movie, request: Request) -> list[dict[str, Any]]:
    movies = _movies(request)
    movies.append(movie.model_dump())
    return movies


@router.put("/{movie_id}", response_model=list[Movie])
def update_movie(
    movie_id: int,
    movie: Movie,
    request: Request,
) -> list[dict[str, Any]]:
    movies = _movies(request)
    for item in movies:
        if item["id"] == movie_id:
            item.update(movie.model_dump(exclude={"id"}))
            break
    return movies


@router.delete("/{movie_id}", response_model=list[Movie])
def delete_movie(movie_id: int, request: Request) -> list[dict[str, Any]]:
    movies = _movies(request)
    for index, movie in enumerate(movies):
        if movie["id"] == movie_id:
            del movies[index]
            return movies
    raise HTTPException(
        status_code=404,
        detail=f"Película con id = {movie_id} no encontrada",
    )
