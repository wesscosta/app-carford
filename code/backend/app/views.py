from flask import Flask, request, jsonify
from app import db
from datetime import datetime
from .models import Owner, Vehicle as Car


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
    description = request.json['description']
    owner.update(dict(description = description, created_at = datetime.utcnow()))
    db.session.commit()
    return {'owner': format_owner(owner)}



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

