import matplotlib.pyplot as plt
from sqlalchemy.orm import Session
from . import models


def generate_image(db: Session, product_name: str):
    products = db.query(models.Product).filter(models.Product.name == product_name).all()

    days = [product.datetime.strftime("%d/%m/%Y") for product in products]
    prices = [product.price for product in products]

    fig, ax = plt.subplots()
    bar_container = ax.bar(days, prices)
    ax.set(ylabel='Цены в usd($)', title=f"Динамика роста цены товара \'{product_name}\'")
    ax.title.set_size(8)
    ax.bar_label(bar_container, fmt='{:,.0f}')

    plt.savefig("sql_app/images/statistics.png", dpi=120)
