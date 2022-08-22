from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:password@localhost/carford'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    description = db.Column(db.String(100),nullable=False)
    create_at = db.Column(db.DataTime, nullLable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Event: {self.description}"

    def __init__ (self, description):
        self.description = description

@app.route('/')
def hello():
    return 'Hey!'

if __name__ == '__main__':
    app.run()
