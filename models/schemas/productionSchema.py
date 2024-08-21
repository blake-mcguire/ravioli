from marshmallow import Schema, fields
from . import ma  

class ProductionSchema(ma.Schema):
    id = fields.Integer(dump_only=True) 
    product_id = fields.Integer(required=True)  
    quantity = fields.Integer(required=True)
    production_date = fields.Date(required=True)

    # Optional: Nested Product data
    product = fields.Nested('ProductSchema', only=['id', 'name'])

    class Meta:
        fields = ('id', 'product_id', 'quantity', 'production_date', 'product')



production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)
