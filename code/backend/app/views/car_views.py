from flask import request, jsonify
from app import app, db
from models import Car



## Car and/or Vehicle
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

