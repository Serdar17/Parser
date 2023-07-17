from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///price.sqlite")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Product(Base):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float)

Base.metadata.create_all(engine)
