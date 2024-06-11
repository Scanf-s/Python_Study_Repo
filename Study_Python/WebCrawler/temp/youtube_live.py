import time
from random import randint
from typing import List, Tuple, Any

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

def init_driver():
    user_info = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    service = Service(ChromeDriverManager().install())

    options: Options = Options()
    options.add_experimental_option("detach", True)  # Keep browser open
    options.add_experimental_option('excludeSwitches', ['disable-popup-blocking', 'enable-automation'])  # Disable popup
    options.add_argument("window-size=800,1280")  # Set window size
    options.add_argument("incognito")  # Secret mode
    # options.add_argument("--headless") # Run in background
    options.add_argument("--mute-audio")  # Mute audio
    options.add_argument(f"user-agent={user_info}")

    new_driver: WebDriver = webdriver.Chrome(options=options, service=service)
    return new_driver

def scroll(driver):
    last_height: int = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(randint(1, 4))

        new_height: int = driver.execute_script("return document.documentElement.scrollHeight")
        if new_height == last_height:
            break

        last_height = new_height


def press_show_all(driver):
    """
    모두보기 버튼 클릭
    """
    contents: WebElement = driver.find_element(By.ID, "contents")
    first_section: WebElement = contents.find_element(By.TAG_NAME, "ytd-rich-section-renderer")
    menu_container: WebElement = first_section.find_element(By.ID, "menu-container")
    ActionChains(driver).move_to_element(menu_container).click().perform()
    time.sleep(5)


def get_live_details(driver) -> tuple[List[Any], List[str], List[str], List[str]]:
    """
    thumbnail_list : 썸네일 이미지 링크 리스트
    title_list : 방송 제목 리스트
    channel_name_list : 채널 주인장 이름 리스트
    live_viewers_list : 시청자 수 리스트
    """
    page: str = driver.page_source
    soup: BeautifulSoup = BeautifulSoup(page, "html.parser")

    thumbnail_list: List = [img['src'] for yt_image in soup.find_all("yt-image") for img in yt_image.find_all("img") if 'src' in img.attrs]
    title_list: List = [title.text for title in soup.find_all("yt-formatted-string", id="video-title")]
    channel_name_list: List = [channel_name.text for text_container in soup.find_all("div", {"id": "text-container"}) for channel_name in text_container.find_all('a')]
    live_viewers_list: List = [viewers.text for viewers in soup.find_all("span", class_="inline-metadata-item style-scope ytd-video-meta-block")]
    return thumbnail_list, title_list, channel_name_list, live_viewers_list

def main(driver):
    url: str = "https://www.youtube.com/channel/UC4R8DWoMoI7CAwX8_LjQHig"
    driver.get(url)
    time.sleep(5)

    try:
        # 모두보기 버튼 클릭
        press_show_all(driver)

        # 페이지 끝까지 내리기
        scroll(driver)

        thumbnail_list, title_list, channel_name_list, live_viewers_list = get_live_details(driver)
        print(*thumbnail_list)
        print(*title_list)
        print(*channel_name_list)
        print(*live_viewers_list)


    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # 참고 블로그 :
    # https://m.blog.naver.com/ksg97031/222070026332
    # https://m.blog.naver.com/lmj4160/222462966573
    driver: WebDriver = init_driver()
    main(driver)
