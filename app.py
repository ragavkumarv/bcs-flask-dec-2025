# save this as app.py
from flask import Flask
from routes.movies_bp import movies_bp
from routes.users_bp import users_bp
from config import Config
from extensions import db
from sqlalchemy.sql import text


app = Flask(__name__)
app.config.from_object(Config)  # URL

db.init_app(app)  # call button


# Testing DB Connection
with app.app_context():
    try:
        result = db.session.execute(text("SELECT 1")).fetchall()
        print("Connection successful:", result)
    except Exception as e:
        print("Error connecting to the database:", e)

# Task
# /api/movies - JSON


# @ -> Decorator -> HOF
@app.get("/")
def hello():
    return "<h1>Hello, World! 🎉 🔥</h1>"


app.register_blueprint(movies_bp, url_prefix="/api/movies")
app.register_blueprint(users_bp, url_prefix="/api/auth")

# Task
# 1. Postman - create 3 Api
# 2. Handle Not Found
# 3. Delete movie

# Delete

# BluePrint
# 1. Organizing
# 2. Template - Scale
