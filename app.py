# save this as app.py
from flask import Flask
from routes.movies_bp import movies_bp


app = Flask(__name__)


# Task
# /api/movies - JSON


# @ -> Decorator -> HOF
@app.get("/")
def hello():
    return "<h1>Hello, World! 🎉 🔥</h1>"


app.register_blueprint(movies_bp, url_prefix="/api/movies")
# Task
# 1. Postman - create 3 Api
# 2. Handle Not Found
# 3. Delete movie

# Delete

# BluePrint
# 1. Organizing
# 2. Template - Scale
