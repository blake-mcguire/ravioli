from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from typing import List

class Employee(Base):
    __tablename__ = 'Employees'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False, unique=True)
    
    # One-to-Many: Employee and Products
    products: Mapped[List["Product"]] = db.relationship("Product", back_populates="employee")
