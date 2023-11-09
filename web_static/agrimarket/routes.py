#!/usr/bin/env python3

from flask import render_template
from app import app

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/products')
def products():
    products_data = [
        {"name": "Product 1", "description": "Description 1"},
        {"name": "Product 2", "description": "Description 2"},
        # Add more product data as needed
    ]
    return render_template('products.html', products=products_data)

@app.route('/blog')
def blog():
    blog_data = [
        {"title": "Article 1", "content": "Content of Article 1"},
        {"title": "Article 2", "content": "Content of Article 2"},
        # Add more blog articles as needed
    ]
    return render_template('blog.html', blog=blog_data)

@app.route('/equipment')
def equipment():
    equipment_data = [
        {"name": "Equipment 1", "description": "Description 1"},
        {"name": "Equipment 2", "description": "Description 2"},
        # Add more equipment data as needed
    ]
    return render_template('equipment.html', equipment=equipment_data)
