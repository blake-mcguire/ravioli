from marshmallow import fields
from . import ma

class EmployeeSchema(ma.Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)
    products = fields.Nested('ProductSchema', many=True, only=["id", "name", "price"])  # Nested relationship to products

    class Meta:
        fields = ("id", "name", "products")

employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)

