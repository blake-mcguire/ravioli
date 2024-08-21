from sqlalchemy import func
from models.product import Product
from models.production import Production
from database import db

def get_total_quantity_by_product_on_date(specific_date):
    query = db.session.query(
        Product.name.label('product_name'),
        func.sum(Production.quantity).label('total_quantity_produced')
    ).join(Production, Product.id == Production.product_id).filter(Production.production_date == specific_date).group_by(Product.name)
    
    results = db.session.execute(query).fetchall()
    return results


def create_production_record(product_id, quantity, production_date):
    new_production = Production(
        product_id=product_id,
        quantity=quantity,
        production_date=production_date
    )
    db.session.add(new_production)
    db.session.commit()
    return new_production