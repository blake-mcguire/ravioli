from flask import Blueprint
from controllers.productionController import total_quantity_by_product_on_date,create_production

production_blueprint = Blueprint('production_bp', __name__)
production_blueprint.route('/total-quantity-by-product-on-date', methods=['GET'])(total_quantity_by_product_on_date)
production_blueprint.route('/create-production', methods=['POST'])(create_production)