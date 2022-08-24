# Import installed packages
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

# Model table owner
class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DataTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Owner: {self.description}"
    
    def __init__(self, description):
        self.description = description

# Model table car
class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True,nullable=False)
    content = db.Column(db.String(120), unique=True, nullable=False)
        
    def __init__(self, title, content):
        self.title = title
        self.content = content
            
db.create_all()

@app.route("/")
def index():
    return "<h2>Esta é a página inicial<h2>"

@app.route("/api/")
def root():
    return jsonify({"message": "API carford"})

def format_owner(owner):
    return{
        "description":owner.description,
        "id":owner.id,
        "created_at":owner.created
    }

# create an owners
@app.route('/owner', methods=['POST'])
def create_owner():
    description = request.json['description']
    owner = Owner(description)
    db.session.add(owner)
    db.session.commit()
    return format_owner(owner)

# get all owners
@app.route('/owners', methods=['GET'])
def get_owners():
    owners = Owner.query.order_by(Owner.id.asc()).all()


@app.route('/Cars/<id>', methods=['GET'])
def get_Car(id):
    Car = Car.query.get(id)
    del Car.__dict__['_sa_instance_state']
    return jsonify(Car.__dict__)

@app.route('/Cars', methods=['GET'])
def get_Cars():
    Cars = []
    for Car in db.session.query(Car).all():
        del Car.__dict__['_sa_instance_state']
        Cars.append(Car.__dict__)
    return jsonify(Cars)

@app.route('/Cars', methods=['POST'])
def create_Car():
    body = request.get_json()
    db.session.add(Car(body['title'], body['content']))
    db.session.commit()
    return "Car created"

@app.route('/Cars/<id>', methods=['PUT'])
def update_Car(id):
    body = request.get_json()
    db.session.query(Car).filter_by(id=id).update(
        dict(title=body['title'], content=body['content']))
    db.session.commit()
    return "Car updated"

@app.route('/Cars/<id>', methods=['DELETE'])
def delete_Car(id):
    db.session.query(Car).filter_by(id=id).delete()
    db.session.commit()
    return "Car deleted"

