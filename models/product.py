from database import db, Base  # Import the database instance and base model
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional, List

class Product(Base):
    __tablename__ = "Products"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    employee_id: Mapped[Optional[int]] = mapped_column(db.ForeignKey('Employees.id'), nullable=False)

    # Relationship to Employee
    employee: Mapped["Employee"] = db.relationship("Employee", back_populates="products")


    productions: Mapped[List["Production"]] = db.relationship("Production", back_populates="product")



