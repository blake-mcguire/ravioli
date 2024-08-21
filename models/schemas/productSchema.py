from marshmallow import fields
from . import ma  # Import the Marshmallow instance

class ProductSchema(ma.Schema):
    id = fields.Integer(dump_only=True)  # Auto-generated primary key
    name = fields.String(required=True)
    price = fields.Float(required=True)
    employee = fields.Nested('EmployeeSchema', only=["id", "name"])  # Nested relationship to employee

    class Meta:
        fields = ("id", "name", "price", "employee")

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

