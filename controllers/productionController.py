from flask import request, jsonify
from services import productionService  
from models.schemas.productionSchema import production_schema

def total_quantity_by_product_on_date():
    specific_date = request.args.get('date')  # Expecting date in 'YYYY-MM-DD' format
    results = productionService.get_total_quantity_by_product_on_date(specific_date)
    return jsonify([dict(row) for row in results]), 200


def create_production():
    
    data = request.json
    production_data = production_schema.load(data)
    new_production = productionService.create_production_record(
        product_id=production_data['product_id'],
        quantity=production_data['quantity'],
        production_date=production_data['production_date']
    )
    

    return production_schema.jsonify(new_production), 201