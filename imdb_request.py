import requests
from bs4 import BeautifulSoup as bs

# Парсинг сайта с фильмами https://www.imdb.com/ при помощи модуля request

PRODUCT_URL = "https://www.imdb.com/title/tt2085059/?ref_=hm_top_tt_i_1"

headers = {
    "accept": "*/*",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "text/plain;charset=UTF-8",
    "sec-ch-ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "no-cors",
    "sec-fetch-site": "cross-site",
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
        " Chrome/114.0.0.0 Safari/537.36"
}

page = requests.get(url=PRODUCT_URL, headers=headers)
html = page.text

soup = bs(html, "lxml")
title = soup.find("span", class_="sc-afe43def-1 fDTGTb")
print(f"Название фильма: {title.get_text()}")

rating = soup.find("span", class_="sc-bde20123-1 iZlgcd")
print(f"Рейтинг фильма: {rating.get_text()}/10")

views = soup.find("div", class_="sc-bde20123-3 bjjENQ")
print(f"Количество просмотров: {views.get_text()}")

