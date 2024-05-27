import requests
from bs4 import BeautifulSoup
from datetime import datetime

keyword = input("Search : ")

url = f"https://www.coupang.com/np/search?component=&q={keyword}&channel=user"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"
}
html = requests.get(url=url, headers=headers, timeout=10).text
soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product]")

for rank, item in enumerate(items, 1):
    name = item.select_one(".name")
    price = item.select_one(".price-value")
    link = item.a["href"]
    img_src = item.select_one(".search-product-wrap-img")

    print(f"{rank} {name.text} {price.text} {link} {img_src['src']}")
    if rank == 10:
        break

now = datetime.now()
today = f"{now.year}-{now.month}-{now.day}"

file_name = "index.html"
title_text = f"오늘의 추천 향수"
product_text = f"향수"