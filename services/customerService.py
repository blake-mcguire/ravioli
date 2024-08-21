from database import db #need db be to serve incoming data to db
from models.customer import Customer 
from models.order import Order
from models.product import Product
from models.orderProduct import order_product
from utils.util import encode_token
from sqlalchemy import select, func

from sqlalchemy import select

def login(username, password): #Login using unique info so we don't query multiple users
    query = select(Customer).where(Customer.username == username)
    customer = db.session.execute(query).scalar_one_or_none() #Query customer table for a customer with the password and username

    if customer and customer.password == password:#if we have a customer associated with the username, validated the password
        auth_token = encode_token(customer.id, customer.role.role_name)

        response = {
            "status":"success",
            "message":"Successfully Logged In",
            "auth_token": auth_token
        }
        return response


def save(customer_data):
    
    new_customer = Customer(name=customer_data['name'], email=customer_data['email'], password=customer_data['password'], phone=customer_data['phone'], username=customer_data['username'])
    db.session.add(new_customer)
    db.session.commit()

    db.session.refresh(new_customer)
    return new_customer

def find_all():
    query = select(Customer)
    all_customers = db.session.execute(query).scalars().all()
    return all_customers

def find_all_paginate(page, per_page):
    customers = db.paginate(select(Customer), page = page, per_page = per_page)
    return customers

def get_total_order_value_by_customer(threshold):
    query = db.session.query(
        Customer.name.label('customer_name'),
        func.sum(Product.price * order_product.c.quantity).label('total_order_value')
    ).join(Order, Customer.id == Order.customer_id).join(order_product, Order.id == order_product.c.order_id).join(Product, order_product.c.product_id == Product.id).group_by(Customer.name).having(func.sum(Product.price * order_product.c.quantity) >= threshold).order_by(func.sum(Product.price * order_product.c.quantity).desc())
    
    results = db.session.execute(query).fetchall()
    return results