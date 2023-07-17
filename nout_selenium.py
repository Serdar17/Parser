from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs

# Парсинг интернет магазина https://nout.uz/ основной страницы с товарами при помощи модуля selenium

PRODUCT_URL = "https://nout.uz/?utm_source=google&utm_medium=cpc&utm_campaign=nout_12014084042_search_&utm_content=" \
              "gid_112847615701_g_c_1028523_574191900169&utm_term=nout%20uz_p_/"

with webdriver.Chrome() as driver:
    driver.get(PRODUCT_URL)

    time.sleep(5)

    html = driver.page_source

    soup = bs(html, "lxml")
    for div in soup.find_all("div", class_="product-inner product-item__inner"):
        description = []
        title = div.find_next("h2", class_="woocommerce-loop-product__title")
        print(f"Название товара: {title.get_text()}")

        divs = div.findNext("div", class_="custom-product-attributes").findAll("span")
        for span in divs:
            description.append(f"{span.get_text()}")

        text = '\n'.join(description)
        print(f"Описание товара: {text}")

        price = div.find_next("div", class_="usd-price")
        if price is not None:
            print(f"Цена товара в usd: {price.get_text()}")

        print()
