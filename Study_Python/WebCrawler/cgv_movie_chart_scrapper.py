import requests
from bs4 import BeautifulSoup

# 사이트 접속 -> F12 -> 네트워크 -> 헤더에서 User-Agent 정보 볼 수 있음
header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

base_url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"
html = requests.get(url=base_url, headers=header_user).text

soup = BeautifulSoup(html, "html.parser")
movie_list = soup.select(".sect-movie-chart ol li")

# 19개 초과로 가져오려면 Selenium으로 마우스 조작해야함
for i, movie in enumerate(movie_list):
    if i >= 19:
        break

    movie_rank = movie.select_one(".rank")
    movie_title = movie.select_one(".box-contents a strong.title")
    movie_ticket_sales = movie.select_one(".percent span")
    movie_release_date = movie.select_one(".txt-info strong")

    print(
        {
            "movie_rank": movie_rank.text,
            "movie_title": movie_title.text,
            "movie_ticket_sales": movie_ticket_sales.text,
            "movie_release_date": ' '.join(movie_release_date.text.split())
        }
    )
