from flask import jsonify, request
from models.schemas.orderSchema import order_schema, orders_schema
from marshmallow import ValidationError
from services import orderService

def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as err:
            return jsonify(err.message), 400
    
    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201

def find_all():
     all_orders = orderService.find_all()
     return orders_schema.jsonify(all_orders), 200

def find_by_id(id):
     orders = orderService.find_by_id(id)
     return orders_schema.jsonify(orders), 200

def find_by_customer_id(id):
     orders = orderService.find_by_customer_id(id)
     return orders_schema.jsonify(orders), 200

def find_by_customer_email():
     email = request.json['email']
     orders = orderService.find_by_customer_email(email)
     return orders_schema.jsonify(orders), 200