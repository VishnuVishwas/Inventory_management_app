# app/admin/routes.py

from app import app, db
from flask import render_template, flash, request, redirect
from app.admin.models import Admin
from app.users.models import SignupUser
from flask_login import login_user, logout_user

# signup admin
@app.route('/signup-admin', methods=['GET', 'POST'])
def signup_admin():
    if request.method == 'POST':
        admin_name = request.form['admin_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
           
        existing_admin = Admin.query.filter_by(admin_name=admin_name).first()
        existing_email = Admin.query.filter_by(email=email).first()

        if existing_admin or existing_email:
            flash('Admin name or Email already exists.', 'danger')
            return redirect('/signup-admin')
        
        if password != confirm_password:
            flash('Password did not match. Please try again.', 'danger')
            return redirect('/signup-admin')
        
        new_admin = Admin(admin_name=admin_name, email=email, password=password)
        db.session.add(new_admin)
        db.session.commit()

        flash('Admin created successfully. Please log in.', 'success')
        return redirect('/login-admin')
    
    return render_template('admin/signup_admin.html')

# admin login
@app.route('/login-admin', methods=['GET', 'POST'])
def login_admin():
    if request.method == 'POST':
        email = request.form['email'] 
        password = request.form['password']

        admin = Admin.query.filter_by(email=email).first()

        if not admin or admin.password != password:
            flash('Invalid email or password.', 'danger')
            return redirect('/login-admin')
        
        login_user(admin)  
        flash('Logged in successfully.', 'success')
        return redirect('/view-users')
    
    return render_template('admin/login_admin.html')

# admin logout
@app.route('/logout')
def logout_admin():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect('/')

# view users 
@app.route('/view-users')
def view_users():
    users = SignupUser.query.all()
    return render_template('admin/view_users.html', users=users)

# Block user
@app.route('/block-user/<int:user_id>', methods=['POST'])
def block_user(user_id):
    user = SignupUser.query.get(user_id)
    if user:
        user.blocked = True
        db.session.commit()
        flash('User has been blocked.', 'success')
    else:
        flash('User not found.', 'danger')
    return redirect('/view-users')

# Unblock user
@app.route('/unblock-user/<int:user_id>', methods=['POST'])
def unblock_user(user_id):
    user = SignupUser.query.get(user_id)
    if user:
        user.blocked = False
        db.session.commit()
        flash('User has been unblocked.', 'success')
    else:
        flash('User not found.', 'danger')
    return redirect('/view-users')
