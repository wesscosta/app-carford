
from app import db
from datetime import datetime
import enum

class ColorsCarEnum(enum.Enum):
    amarelo = 'amarelo'
    azul = 'azul'
    cinza = 'cinza'

class ModelsCarEnum(enum.Enum):
    escotilha = 'escotilha'
    sedan = 'sedan'
    conversivel = 'conversivel'

class Owner(db.Model):
    __tablename__ = "owners"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    oweneres = db.relationship('Owner', backref='owners', lazy=True)

    def __repr__(self):
        return f"Owner: {self.name}"
    
    def __init__(self, name):
        self.name = name

class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.Enum(ModelsCarEnum), nullable=False)
    color = db.Column(db.Enum(ColorsCarEnum), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __repr__(self):
        return f"Car: {self.model}"
    
    def __init__(self, model, color, owner):
        self.model = model
        self.color = color
        self.owner_id = owner
