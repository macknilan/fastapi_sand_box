"""
Router for Movies
"""
from typing import Dict, List

# Python

# Pydantic

# fastpi
from fastapi import APIRouter, status, HTTPException, Path, Depends, Query
from fastapi.responses import JSONResponse

# Model

from api.models.movies import Movies

# Security

from api.security_manager import security_manager


router = APIRouter(prefix="/movies", tags=["Movies"])


movies_list = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los seres que ...",
        "year": "2009",
        "rating": 8.0,
        "category": "Action",
    },
    {
        "id": 2,
        "title": "Free Guy",
        "overview": "En un exuberante planeta llamado Pandora viven los Navi, seres que ...",
        "year": "1996",
        "rating": 4.8,
        "category": "Comedy",
    },
    {
        "id": 3,
        "title": "The Lost City",
        "overview": "En un exuberante planeta llamado Pandora viven los.",
        "year": "2004",
        "rating": 2.8,
        "category": "Drama",
    },
    {
        "id": 4,
        "title": "Eternals",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2000",
        "rating": 7.7,
        "category": "Horror",
    },
]

movies_list_update: dict[str, float | str | int] = {
    "title": "Movie title",
    "overview": "Description of the movie",
    "year": 2001,
    "rating": 9.1,
    "category": "Action",
}


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    summary="List movies",
    response_model=list[Movies],
    dependencies=[Depends(security_manager.JWTBearer())],
)
async def get_movies() -> JSONResponse:
    """
    Obtener listado de películas y servicio protegido.
    """
    return JSONResponse(content=movies_list)


@router.get(
    "/list_movies_parameter{movie_id}",
    response_model=Movies,
    status_code=status.HTTP_200_OK,
    summary="List movies by ID",
)
async def get_movie(movie_id: int):
    """
    Obtener película por parámetro ID
    """
    filtered_list_movies = list(filter(lambda x: movie_id == x["id"], movies_list))
    list_movies = list(filtered_list_movies)
    if not list_movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found!"
        )

    return JSONResponse(content=list_movies)


@router.get(
    "/category/",
    response_model=list[Movies],
    status_code=status.HTTP_200_OK,
    summary="Get movies by Query Parameter -category-",
)
async def get_movie_category(
    category: str = Query(min_length=5, max_length=15)
) -> List[Movies]:
    """
    Obtener película por categorías por Query Parameters y se validan por medio de -Query-
    """
    filtered_list_movies = list(
        filter(lambda x: category == x["category"], movies_list)
    )
    list_movies = list(filtered_list_movies)
    if not list_movies:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Movie not found! t(-_-t)"
        )

    return JSONResponse(content=list_movies)


@router.post(
    "/create/",
    response_model=Movies,
    status_code=status.HTTP_201_CREATED,
    summary="Create movie",
)
async def create_movie(movie: Movies):
    """
    Crear una película por parámetros en el body
    """
    movies_list.append(movie)
    return JSONResponse(content={"message": "Se a registrado la película"})


@router.put(
    "/update/{movie_id}",
    response_model=Movies,
    status_code=status.HTTP_201_CREATED,
    summary="Update movie",
)
async def update_movie(
    movie_id: int = Path(
        gt=0,
        title="The ID of the movie.",
        description="This is the ID movie. It's required.",
        example=1,
    ),
    movie_to_update: dict = movies_list_update,
):
    """
    Actualizar una película por parámetros en el body buscando por el parámetro de ID
    """
    filtered_list_movies = list(filter(lambda x: movie_id == x["id"], movies_list))
    if not filtered_list_movies:
        raise HTTPException(status_code=404, detail="Movie not found! t(-_-t)")
    else:
        filtered_list_movies[0].update(
            {
                "id": movie_id,
                "title": movie_to_update["title"],
                "overview": movie_to_update["overview"],
                "year": movie_to_update["year"],
                "rating": movie_to_update["rating"],
                "category": movie_to_update["category"],
            }
        )
    return JSONResponse(content=filtered_list_movies[0])


@router.delete(
    "/delete/{movie_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete movie",
    response_model=dict,
)
async def delete_movie(movie_id: int):
    """
    Eliminar una película por el parámetro de ID
    """
    filtered_list_movies = list(filter(lambda x: movie_id == x["id"], movies_list))
    list_movies = list(filtered_list_movies)
    if not list_movies:
        raise HTTPException(status_code=404, detail="Movie not found! t(-_-t)")
    else:
        movies_list.pop(0)

    return JSONResponse(content={"message": "Se ha eliminado la película"})
