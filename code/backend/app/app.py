from flask import Flask, jsonify
from .models import db, migrate
from app import views

def create_app():

    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)
    migrate.init_app(app, db)

    @app.route("/")
    def index():
        return "<h2>Esta é a página inicial<h2>"

    @app.route("/api/")
    def root():
        return jsonify({"message": "API app carford"})

    return app