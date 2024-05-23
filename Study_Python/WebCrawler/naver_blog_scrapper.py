from bs4 import BeautifulSoup
import requests

# 사이트 접속 -> F12 -> 네트워크 -> 헤더에서 User-Agent 정보 볼 수 있음
header_user = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

base_url = "https://search.naver.com/search.naver?ssc=tab.blog.all&sm=tab_jum&query="
keyword = input("검색어 : ")
html = requests.get(url=base_url+keyword, headers=header_user).text

soup = BeautifulSoup(html, "html.parser")
containers = soup.select(".view_wrap")
print(len(containers))
for container in containers:
    if container.select_one(".link_ad"):
        continue
    title_link = container.select_one(".title_link")
    post_writer = container.select_one(".name")
    post_describe = container.select_one(".dsc_link")

    if title_link and post_writer and post_describe:
        print(f"작성자 : {post_writer.text}", end="\n")
        print(f"링크 : {title_link['href']}", end="\n")
        print(f"제목 : {title_link.text}", end="\n")
        print(f"요약 : {post_describe.text}", end="\n\n")
