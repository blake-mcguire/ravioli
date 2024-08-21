from database import db, Base  
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, Date, ForeignKey

class Production(Base):
    __tablename__ = "Production"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('Products.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    production_date = Column(Date, nullable=False)


    product = relationship("Product", back_populates="productions")
