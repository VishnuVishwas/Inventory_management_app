# app/__init__.py

from flask import Flask, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from secret import SECRET_KEY, SQLALCHEMY_DATABASE_URI

# flask app instance
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

# instance to use hash
bcrypt = Bcrypt(app)

# initialize flask-login
login_manager = LoginManager(app)

# Unauthorized user handler 
@login_manager.unauthorized_handler
def unauthorized():
    flash('You need to log in first.', 'danger')
    return redirect('/login-user')

# load user and login
@login_manager.user_loader
def load_user(user_id):
    from app.users.models import SignupUser
    from app.admin.models import Admin

    user = SignupUser.query.get(int(user_id))
    if user:
        return user
    
    admin = Admin.query.get(int(user_id))
    if admin:
        return admin

# db instance
db = SQLAlchemy(app)

from app.admin import routes
from app.users import routes
from app.products.models import Products
from app.products import routes
from app.users.models import SignupUser
from app.admin.models import Admin