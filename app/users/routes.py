# app/users/routes

from app import app, db, bcrypt
from flask import render_template, request, flash, redirect
from app.users.models import SignupUser
from flask_login import login_user, logout_user

# home
@app.route('/')
def index():
    return render_template('home.html')

# user signup route
@app.route('/signup-user', methods=['GET', 'POST'])
def signup_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        existing_user = SignupUser.query.filter_by(username=username).first()
        existing_email = SignupUser.query.filter_by(email=email).first()

        if existing_user or existing_email:
            flash('Username or Email already exists.', 'danger')
            return redirect('/signup-user')
        
        if password != confirm_password:
            flash('Password did not match. Please try again.', 'danger')
            return redirect('/signup-user')
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        
        new_user = SignupUser(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return redirect('/login-user')
    return render_template('user/signup.html')

# user login route
@app.route('/login-user', methods=['GET', 'POST'])
def login_user_route():

    if request.method == 'POST':
        email = request.form['email'] 
        password = request.form['password']

        user = SignupUser.query.filter_by(email=email).first()

        if user.blocked:
            flash("You are blocked by admin", 'danger')
            return redirect('/')

        if not user or bcrypt.check_password_hash(user.password, password):
            flash('Invalid email or password.', 'danger')
            return redirect('/login-user')
        
        login_user(user)  
        flash('Logged in successfully.', 'success')
        return redirect('/products-page')
    return render_template('user/login.html')

# logout route
@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect('/')

