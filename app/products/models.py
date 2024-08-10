# app/products/models.py

from app.users.models import SignupUser
from app import db
from datetime import datetime

# Products model 
class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(200), nullable=False)
    price = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('signup_user.id'), nullable=False)
    user_name = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Product('{self.name}', '{self.price}', '{self.category}', '{self.user_name}')"
    