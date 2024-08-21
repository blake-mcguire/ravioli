from flask import Blueprint
from controllers.customerController import save, find_all, find_all_paginate, login, total_order_value_by_customer

customer_blueprint = Blueprint('customer_bp', __name__)

customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(find_all)
customer_blueprint.route('/paginate', methods=['GET'])(find_all_paginate)
customer_blueprint.route('/login', methods=['POST'])(login)
customer_blueprint.route('/total-order-value-by-customer', methods=['GET'])(total_order_value_by_customer)
