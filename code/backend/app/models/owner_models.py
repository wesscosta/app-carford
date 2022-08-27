from app import db
from datetime import datetime
from sqlalchemy.orm import relationship

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