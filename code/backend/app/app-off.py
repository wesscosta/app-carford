from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from .models import owner_models, car_models

db.create_all()

from .views import owner_views, car_views

@app.route("/")
def index():
    return "<h2>Página inicial<h2>"

@app.route("/api/")
def root():
    return jsonify({"message": "API app carford"})
