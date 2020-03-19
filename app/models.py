from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    __bind_key__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Aadhar(UserMixin, db.Model):
    __bind_key__ = 'aadhar'
    id = db.Column(db.Integer, primary_key=True)
    docid = db.Column(db.String(16), index=True, unique=True)
    firstname = db.Column(db.String(64), index=True, unique=False)
    lastname = db.Column(db.String(64), index=True, unique=False)

    def set_data(self, did, fn, ln):
        self.docid = generate_password_hash(did)
        self.firstname = generate_password_hash(fn)
        self.lastname = generate_password_hash(ln)

    def check_data(self, did, fn, ln):
        return (check_password_hash(self.docid, did) and check_password_hash(self.firstname, fn) and check_password_hash(self.lastname, ln))

class PAN(UserMixin, db.Model):
    __bind_key__ = 'pan'
    id = db.Column(db.Integer, primary_key=True)
    docid = db.Column(db.String(16), index=True, unique=True)
    firstname = db.Column(db.String(64), index=True, unique=False)
    lastname = db.Column(db.String(64), index=True, unique=False)

    def set_data(self, did, fn, ln):
        self.docid = generate_password_hash(did)
        self.firstname = generate_password_hash(fn)
        self.lastname = generate_password_hash(ln)

    def check_data(self, did, fn, ln):
        return (check_password_hash(self.docid, did) and check_password_hash(self.firstname, fn) and check_password_hash(self.lastname, ln))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
