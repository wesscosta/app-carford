from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
import enum

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

# ----- MODELS ----------- 
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

# -----------CREATE DATABASE----------------
# db.create_all()

#------------- VIEWS------------
@app.route("/")
def index():
    return "<h2>Esta é a página inicial<h2>"

@app.route("/api/")
def root():
    return jsonify({"message": "API app carford"})


def format_owner(owner):
    return{
        "name":owner.name,
        "id":owner.id,
        "created_at":owner.created
    }

# create an owners
@app.route('/owner', methods=['POST'])
def create_owner():
    name = request.json['name']
    owner = Owner(name)
    db.session.add(owner)
    db.session.commit()
    return format_owner(owner)

# get all owners
@app.route('/owners', methods=['GET'])
def get_owners():
    owners = Owner.query.order_by(Owner.id.asc()).all()
    owner_list = []
    for owner in owners:
        owner_list.append(format_owner(owner))
    return {'owners': owner_list}

@app.route('/owners/<id>', methods =['GET'])
def get_owner(id):
    # if request.method == 'GET':
    owner = Owner.query.filter_by(id=id).one()
    format_owner = format_owner(owner)
    return {'owner': format_owner}

# delete an owner
@app.route('/owners/<id>', methods = ['DELETE'])
def delete_owner(id):
    owner =  Owner.query.filter_by(id=id).one()
    db.session.delete(owner)
    db.session.commit()
    return f'Owner (id: {id}) deleted!'

# update an owner
@app.route('/owner/<id>', methods = ['PUT'])
def update_owner(id):
    owner = Owner.query.filter_by(id=id)
    name = request.json['name']
    owner.update(dict(name = name, created_at = datetime.utcnow()))
    db.session.commit()
    return {'owner': format_owner(owner)}


