from models.product import Product
from models.employee import Employee
from models.orderProduct import order_product
from models.order import Order
from database import db
from sqlalchemy import select, func

def save(product_data):
    new_product = Product(name=product_data['name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)

    return new_product

def find_all():
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def search_product(search_term):
    query = select(Product).where(Product.name.like(f'%{search_term}%'))
    search_products = db.session.execute(query).scalars().all()
    return search_products

def get_all_products_paginated(page, per_page):
    products = db.session.query(Product).paginate(page=page, per_page=per_page, error_out=False)
    return products.items

def get_total_quantity_by_employee():
    query = db.session.query(
        Employee.name.label('employee_name'),
        func.count(Product.id).label('total_quantity')
    ).join(Product).group_by(Employee.name)
    
    results = db.session.execute(query).fetchall()
    return results

def get_top_selling_products():
    query = db.session.query(
        Product.name.label('product_name'),
        func.sum(order_product.c.quantity).label('total_quantity_ordered')
    ).join(order_product, Product.id == order_product.c.product_id).group_by(Product.name).order_by(func.sum(order_product.c.quantity).desc())
    
    results = db.session.execute(query).fetchall()
    return results

