from unicodedata import name
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()


class Owner(db.Model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    description = db.Column(db.String(50), nullable=False) # name
    created_at = db.Column(db.DataTime, nullable=False, default=datetime.utcnow)

class Cars(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(20), nullable=False)
    color = db.Column(db.String(20), nullable=False)
    owner_fk = db.Column()