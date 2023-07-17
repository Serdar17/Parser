from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs

# Парсинг сайта с фильмами https://www.imdb.com/ при помощи модуля selenium and bs4

URL = "https://www.imdb.com/"

with webdriver.Chrome() as driver:
    driver.get(URL)

# Из-за медленного интернета стоит большая задержка, т.к не все прогружается
    time.sleep(10)

    html = driver.page_source
    soup = bs(html, "lxml")
    print("---- Топ 10 фильмов недели на https://www.imdb.com/ ----")
    for div in soup.find_all("div", class_="ipc-poster-card")[:10]:
        title = div.find_next("span", attrs={"data-testid": "title"})
        print(f"{title.get_text()}")

        rating = div.find_next("span", class_="ipc-rating-star")
        print(f"Рейтинг: {rating.get_text()}/10")

        a = div.find_next('a', href=True)
        print(f"Ссылка на просмотр: {URL}{a['href']}")
        print()
