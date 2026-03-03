class Config:
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:yourpassword@localhost:5432/movie_bcs_db_dec_2025"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
