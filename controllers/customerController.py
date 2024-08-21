from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService #dont import the individual function, import the module as a whole
from marshmallow import ValidationError
from caching import cache
from utils.util import token_required, admin_required

def login():
    try:
        credentials = request.json
        token = customerService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'messages':'Invalid payload, expecting username and password'}), 401
    
    if token:
        return jsonify(token), 200
    else:
        return jsonify({'messages':'Invalid username or password'}), 401

def save(): #name the controller will always be the same as the service function

    try:
        #try to validate the incoming data, and deserialize
        customer_data = customer_schema.load(request.json)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_data), 201


def total_order_value_by_customer():
    threshold = float(request.args.get('threshold', 0))  # Default threshold is 0
    results = customerService.get_total_order_value_by_customer(threshold)
    return jsonify([dict(row) for row in results]), 200


# @token_required
@cache.cached(timeout=60)
@admin_required
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers),200

def find_all_paginate():
    page = int(request.args.get('page'))
    per_page = int(request.args.get('per_page'))
    customers = customerService.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers), 200