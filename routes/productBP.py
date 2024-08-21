from flask import Blueprint
from controllers.productController import find_all, save, search_product, get_all_products_paginated, total_quantity_by_employee, top_selling_products

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(find_all)
product_blueprint.route('/search', methods=['GET'])(search_product)
product_blueprint.route('/paginate', methods=['GET'])(get_all_products_paginated)
product_blueprint.route('/total-quantity-by-employee', methods=['GET'])(total_quantity_by_employee)
product_blueprint.route('/top-selling-products', methods=['GET'])(top_selling_products)
