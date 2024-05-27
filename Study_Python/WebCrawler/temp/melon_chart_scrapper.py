from bs4 import BeautifulSoup
import requests

# 사이트 접속 -> F12 -> 네트워크 -> 헤더에서 User-Agent 정보 볼 수 있음
header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

base_url = "https://www.melon.com/chart/index.htm"
html = requests.get(url=base_url, headers=header_user).text

soup = BeautifulSoup(html, "html.parser")

# 둘중에 아무거나 써도 작동합니다.
# song_list = soup.select("tbody tr")
song_list = soup.find_all(class_=["lst50", "lst100"])

for song_container in song_list:
    rank = song_container.select_one(".rank")
    rank_wrap_up = song_container.select_one(".rank_wrap .up")
    rank_wrap_up_text = rank_wrap_up.text.strip() + "위 상승" if rank_wrap_up else None
    rank_wrap_down = song_container.select_one(".rank_wrap .down")
    rank_wrap_down_text = rank_wrap_down.text.strip() + "위 하락" if rank_wrap_down else None
    if rank_wrap_up_text:
        rank_wrap_text = rank_wrap_up_text
    elif rank_wrap_down_text:
        rank_wrap_text = rank_wrap_down_text
    else:
        rank_wrap_text = "순위 유지"

    title = song_container.select_one(".rank01 a")
    singer = song_container.select_one(".rank02 a")
    album_name = song_container.select_one(".rank03 a")

    print({
        "rank": rank.text,
        "rank_wrap_text": rank_wrap_text,
        "title": title.text.strip(),
        "singer": singer.text.strip(),
        "album_name": album_name.text.strip()
    })
