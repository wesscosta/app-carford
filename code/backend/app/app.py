from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>Esta é a página inicial<h2>"

@app.route("/api/")
def root():
    return jsonify({"message": "API app carford"})