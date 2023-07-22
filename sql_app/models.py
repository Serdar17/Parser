from sqlalchemy import Column, Integer, String, Float, DateTime

from .database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    datetime = Column(DateTime)

