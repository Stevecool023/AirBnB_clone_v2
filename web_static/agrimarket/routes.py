from flask import render_template
from app import app, db
from app.models import Product, BlogPost, Equipment

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/products')
def products():
    # Fetch products from the database
    products_data = Product.query.all()
    return render_template('products.html', products=products_data)

@app.route('/blog')
def blog():
    # Fetch blog posts from the database
    blog_data = BlogPost.query.all()
    return render_template('blog.html', blog=blog_data)

@app.route('/equipment')
def equipment():
    # Fetch equipment from the database
    equipment_data = Equipment.query.all()
    return render_template('equipment.html', equipment=equipment_data)
