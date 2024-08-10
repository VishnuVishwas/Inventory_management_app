# app/products/routes.py

from app import app, db
from flask import Flask, json, request, jsonify, render_template, redirect
from app.products.models import Products
from app.users.models import SignupUser
from flask_login import login_required, current_user


# get product page
@app.route('/products-page', methods=['GET'])
@login_required
def render_product_page():
    products = Products.query.all()
    return render_template('products/products.html', products=products)

# create a product
@app.route('/products', methods=['POST'])
@login_required
def create_product():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        user = SignupUser.query.filter_by(id=current_user.id).first()
        if user:
            user_name = current_user.username
        else:
            user_name = "Unknown"

        new_product = Products(name=name, price=price, category=category, user_id=current_user.id, user_name=user_name)

        db.session.add(new_product)
        db.session.commit()
        return redirect('/products-page')

    return render_template('products/products.html')
    
# update product
@app.route('/products/<int:id>', methods=['GET', 'POST'])
@login_required
def update_product(id):
    product = Products.query.get_or_404(id)
    
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        category = request.form.get('category')

        # Check for changed fields
        if not name:
            name = product.name
        if not price:
            price = product.price
        if not category:
            category = product.category

        product.name = name
        product.price = price
        product.category = category

        db.session.commit()
        return redirect('/products-page')

    return render_template('products/update.html', product=product)


# delete product
@app.route('/products/delete/<int:id>', methods=['POST'])
@login_required
def delete_product(id):

    if request.method == 'POST':
        if request.form.get('_method') == 'DELETE':
            product = Products.query.get_or_404(id)
            if product:
                db.session.delete(product)
                db.session.commit()
                return redirect('/products-page')
    
    return jsonify({'error': 'Method Not Allowed'}), 405

