from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

class User(db.Model, SerializerMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    _password_hash = db.Column(db.String)

    @validates('username')
    def validates_username(self, key, username):
        if username and len(username) > 0:
            return username
        else:
            raise ValueError("User must have a username!")
        
    @hybrid_property
    def password_hash(self):
        # password should not be visible
        pass

    @password_hash.setter
    def password_hash(self, password):
        # encode password by generating hash
        pass

    def authenticate(self, password):
        # return match of hashed to non-hashed password
        pass

    def __repr__(self):
        return f"Username: {self.username}"