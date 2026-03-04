from models.movie import Movie
from extensions import db
from sqlalchemy import select, func
from app import app

with app.app_context():
    stmt = select(Movie).order_by(Movie.id)
    movies = db.session.execute(stmt).scalars().all()
    for m in movies:
        print(m.id, m.name, m.rating)
