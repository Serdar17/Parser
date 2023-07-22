import requests
from bs4 import BeautifulSoup as bs


PAGE_URL = "https://nout.uz/"


def start_parser():
    page = requests.get(url=PAGE_URL)
    html = page.text

    soup = bs(html, "html.parser")
    products = []

    for div in soup.find_all("div", class_="product-inner product-item__inner"):
        description = []
        title = div.find_next("h2", class_="woocommerce-loop-product__title")

        divs = div.findNext("div", class_="custom-product-attributes").findAll("span")
        for span in divs:
            description.append(f"{span.get_text()}")

        text = '\n'.join(description).replace("/", "|")

        price = div.find_next("div", class_="usd-price")
        if price is not None:
            products.append(
                {
                    "name": title.get_text().replace("/", "|"),
                    "description": text,
                    "price": float(price.get_text())
                }
            )
    return products


if __name__ == "__main__":
    start_parser()