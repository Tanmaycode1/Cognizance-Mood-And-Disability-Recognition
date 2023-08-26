from . import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150),unique = True)
    password = db.Column(db.String(150))
    phone = db.Column(db.String(100))
    name = db.Column(db.String(150))
    type = db.Column(db.String(150))
    appointment = db.relationship('appointments')

class appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patid = db.Column(db.String(1000))
    name = db.Column(db.String(1000))
    time = db.Column(db.String(100))
    date = db.Column(db.String(100))
    number = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


