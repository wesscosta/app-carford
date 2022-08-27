from app import db
import enum

class ColorsCarEnum(enum.Enum):
    amarelo = 'amarelo'
    azul = 'azul'
    cinza = 'cinza'

class ModelsCarEnum(enum.Enum):
    escotilha = 'escotilha'
    sedan = 'sedan'
    conversivel = 'conversivel'


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