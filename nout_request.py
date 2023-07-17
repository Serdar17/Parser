import requests
from bs4 import BeautifulSoup as bs
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from product import Product

# Наполнение БД при помощи парсера без дубликатов

PRODUCT_URL = "https://nout.uz/?utm_source=google&utm_medium=cpc&utm_campaign=nout_12014084042_search_&utm_content=" \
              "gid_112847615701_g_c_1028523_574191900169&utm_term=nout%20uz_p_"

engine = create_engine("sqlite:///price.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

page = requests.get(url=PRODUCT_URL)
html = page.text

soup = bs(html, "html.parser")
products = []

for div in soup.find_all("div", class_="product-inner product-item__inner"):
    description = []
    title = div.find_next("h2", class_="woocommerce-loop-product__title")

    divs = div.findNext("div", class_="custom-product-attributes").findAll("span")
    for span in divs:
        description.append(f"{span.get_text()}")

    text = '\n'.join(description)

    price = div.find_next("div", class_="usd-price")
    if price is not None:
        products.append(
            {
                "name": title.get_text(),
                "description": text,
                "price": float(price.get_text())
            }
        )


for product in products:
    exists_product = session.query(Product).filter_by(name=product["name"]).first()
    if exists_product is not None:
        exists_product.price = product["price"]
    else:
        item = Product(
            name=product["name"],
            description=product["description"],
            price=product["price"]
        )
        session.add(item)
session.commit()
