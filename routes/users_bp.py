# from package_name import function
from flask import Blueprint, request
from models.user import User
from extensions import db
from sqlalchemy import select


# SCREAMING_SNAKE_CASE or CONSTANT_CASE
HTTP_NOT_FOUND = 404
HTTP_SERVER_ERROR = 500
HTTP_USER_ERROR = 400

users_bp = Blueprint("users_bp", __name__)


# Select *
# From Users
# Where username = "jacob"


@users_bp.post("/signup")
def signup_user():
    # Data -> body as json
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    stmt = select(User).where(User.username == username)
    db_user = db.session.execute(stmt).scalars().all()

    if db_user:
        return {"error": "username already taken"}, HTTP_USER_ERROR

    # Table
    # Add the user to the Table

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return new_user.to_dict()

    # new_movie = Movie(
    #     name=data.get("name"),
    #     poster=data.get("poster"),
    #     summary=data.get("summary"),
    #     rating=data.get("rating"),
    #     trailer=data.get("trailer"),
    # )

    # try:
    #     db.session.add(new_movie)  # temp
    #     db.session.commit()  # permanent
    # except Exception as err:
    #     db.session.rollback()  # Undo
    #     return {"message": str(err)}, HTTP_SERVER_ERROR

    # return {"data": new_movie.to_dict(), "message": "movie added successfully"}
