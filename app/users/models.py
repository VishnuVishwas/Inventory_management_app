# app/users/models.py

from app import db
from flask_login import UserMixin

# user model
class SignupUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    blocked = db.Column(db.Boolean, default=False)
    
    def __repr__(self):
        return f"{self.username} created successfully."
