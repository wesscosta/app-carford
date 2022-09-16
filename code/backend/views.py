from flask import request, jsonify
from datetime import datetime
from app import app, db
from models import Owner


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


