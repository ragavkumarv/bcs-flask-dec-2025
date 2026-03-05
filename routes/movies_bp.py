# from package_name import function
from flask import Blueprint, request
from models.movie import Movie
from extensions import db
from sqlalchemy import select


# SCREAMING_SNAKE_CASE or CONSTANT_CASE
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500

movies_bp = Blueprint("movies_bp", __name__)


# List[Movie Object] -> List[Dictionary]
@movies_bp.get("/")
def get_all_movies():
    #  Select * from movies - Black Box - Learning
    data = db.session.execute(select(Movie)).scalars().all()

    all_movies = []
    for movie in data:
        all_movies.append(movie.to_dict())

    return all_movies


# Flask: List[Dict] -> JSON (Auto conversion)


# id -> variable
# {"message": "movie not found"}
@movies_bp.get("/<id>")  # API Endpoint
def get_movie_by_id(id):
    # Select * from movies where id = 100
    data = db.session.get(Movie, id)

    if not data:
        return {"message": "movie not found"}, HTTP_NOT_FOUND

    return data.to_dict()


# get_movie_by_id -> Controller


@movies_bp.delete("/<id>")
def delete_movie_by_id(id):
    movie = db.session.get(Movie, id)

    if not movie:
        return {"message": "movie not found"}, HTTP_NOT_FOUND

    try:
        db.session.delete(movie)  # temp
        db.session.commit()  # permanent
    except Exception as err:
        db.session.rollback()  # Undo
        return {"message": str(err)}, HTTP_SERVER_ERROR

    return {"data": movie.to_dict(), "message": "movie delete successfully"}


@movies_bp.post("/")
def create_movie():
    # Data -> body as json
    data = request.get_json()

    new_movie = Movie(
        name=data["name"],
        poster=data["poster"],
        summary=data["summary"],
        rating=data["rating"],
        trailer=data["trailer"],
    )

    try:
        db.session.add(new_movie)  # temp
        db.session.commit()  # permanent
    except Exception as err:
        db.session.rollback()  # Undo
        return {"message": str(err)}, HTTP_SERVER_ERROR

    return {"data": new_movie.to_dict(), "message": "movie added successfully"}

    # print(data)
    # return data
