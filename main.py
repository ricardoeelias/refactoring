from fastapi import FastAPI

from routers.movies import router as movies_router


app = FastAPI()

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En Pandora, un exmarine parapléjico en un cuerpo biológico sintético (avatar) debe decidir entre ... pueblo indígena Na'vi.",
        "release": "2009-12-18",
        "rating": 8.2,
        "category": "Acción",
        "earnings": 2923700000,
    },
    {
        "id": 2,
        "title": "El hombre de acero",
        "overview": "Un joven alienígena con poderes sobrehumanos enviado a la Tierra desde Krypton debe asumir el rol de héroe ...",
        "release": "2013-12-06",
        "rating": 7.7,
        "category": "Ficción",
        "earnings": 663292147,
    },
    {
        "id": 3,
        "title": "La llegada ",
        "overview": "Comunicación con extraterrestres que llegan a la tierra ...",
        "release": "2016-11-11",
        "rating": 8.5,
        "category": "Ficción",
        "earnings": 203388186,
    },
]

app.state.movies = movies
app.include_router(movies_router)


@app.get("/", tags=["Home"])
def home() -> dict[str, str]:
    return {"mensaje": "¡Hola mundo!"}
