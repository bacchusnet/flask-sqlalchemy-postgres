from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://Riaz:@127.0.0.1:5432/testdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning

# Initialize DB
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

# Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty


# Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# Initialize Schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create/add new
@app.route('/product', methods=['POST'])
def add_product():
    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    new_product = Product(name, description, price, qty)
    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get all
@app.route('/product', methods=['GET'])
def get_all_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result)

# Get one
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    
    return product_schema.jsonify(product)

# Update existing item
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)

# Delete one
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product != None:
        # Successfully found the item we want to delete
        db.session.delete(product)
        db.session.commit()
        return product_schema.jsonify(product)
    else:
        # Can't find the item we want to delete
        return product_schema.jsonify({})

# Base route
@app.route('/', methods=['GET'])
def get():
    return jsonify({"hey":"hi"})



if __name__=='__main__':
    app.run(debug=True)
