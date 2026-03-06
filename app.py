# save this as app.py
from flask import Flask
from routes.movies_bp import movies_bp
from routes.users_bp import users_bp
from config import Config
from extensions import db, jwt
from sqlalchemy.sql import text
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(Config)  # URL
CORS(app)

db.init_app(app)  # call button
jwt.init_app(app)


@jwt.unauthorized_loader
def _unauth(e):
    return {"error": "missing/invalid token"}, 401


@jwt.expired_token_loader
def _expired(h, p):
    return ({"error": "token expired"}), 401


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
