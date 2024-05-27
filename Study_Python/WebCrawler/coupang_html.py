import requests
from bs4 import BeautifulSoup
from datetime import datetime
import ftplib
from ftp_connection_info import ftp_host, ftp_user, ftp_passwd

keyword = input("검색할 상품 : ")
url = f"https://www.coupang.com/np/search?component=&q={keyword}"

header_user = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "accept-language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
req = requests.get(url, timeout=5, headers=header_user)

html = req.text
soup = BeautifulSoup(html, "html.parser")

items = soup.select("[class=search-product]")
main_text = ''
for rank, item in enumerate(items, 1):
    name = item.select_one(".name")
    price = item.select_one(".price-value")
    link = item.a["href"]
    img_src = item.select_one(".search-product-wrap-img")

    print(f"[{rank}]위")
    print(f"제품명 : {name.text}")
    print(f"{price.text}원")
    rocket = item.select_one(".badge.rocket")

    if rocket:
        print("🚀로켓 배송 가능")
    else:
        print("🚀로켓 배송 불가")

    print(f"링크 : https://www.coupang.com{link}")
    if img_src.get("data-img-src"):
        img_url = f"http:{img_src.get('data-img-src')}"
    else:
        img_url = f"http:{img_src.get('src')}"
    img_url = img_url.replace("230x230ex", "600x600ex")
    print(f"이미지 URl: {img_url}")
    print()

    main_text += f"<p><h2>{rank}위 : {name.text}</h2><b>가격 : {price.text}</b></p><div><a href='https://www.coupang.com{link}' target='_blank'><div class='img main'><img src='{img_url}' alt='제품 이미지' /></div></div>"

    if rank == 10:
        break

now = datetime.now()
today = f"{now.year}년 {now.month}월 {now.day}일"

file_name = "index.html"
title_text = f"금주의 추천 {keyword}"
summary_text = f"{today} 기준 추천 {keyword} top 10"
html_text = f"""
    <!DOCTYPE HTML>
    <html>
        <head>
            <title>{title_text}</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
            <link rel="stylesheet" href="assets/css/main.css" />
            <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
        </head>
        <body class="is-preload">
            <!-- Wrapper -->
                <div id="wrapper">
                    <!-- Header -->
                    <header id="header">
                        <a href="index.html" class="logo">쿠팡크롤링</a>
                    </header>

                    <!-- Main -->
                    <div id="main">
                        <!-- Post -->
                        <section class="post">
                            <header class="major">
                                <span class="date">{today}</span>
                                <h1>{title_text}</h1>
                                <p>{summary_text}</p>
                            </header>
                            {main_text}
                        </section>
                    </div>
                </div>
            <!-- Scripts -->
                <script src="assets/js/jquery.min.js"></script>
                <script src="assets/js/jquery.scrollex.min.js"></script>
                <script src="assets/js/jquery.scrolly.min.js"></script>
                <script src="assets/js/browser.min.js"></script>
                <script src="assets/js/breakpoints.min.js"></script>
                <script src="assets/js/util.js"></script>
                <script src="assets/js/main.js"></script>
        </body>
    </html>
"""

with open(f"./{file_name}", "w", encoding="utf-8") as f:
    f.write(f"{html_text}")

ftp = ftplib.FTP()
ftp.connect(ftp_host, 21)
ftp.login(ftp_user, ftp_passwd)

ftp.cwd("./html")

my_file = open(f"./{file_name}", "rb")
ftp.storbinary(f"STOR {file_name}", my_file)
my_file.close()
ftp.quit()
