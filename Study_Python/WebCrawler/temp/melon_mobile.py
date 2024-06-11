import random
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def init_driver():
    user_info = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36"
    service = Service(ChromeDriverManager().install())

    options = Options()
    options.add_experimental_option("detach", True)  # Keep browser open
    options.add_experimental_option('excludeSwitches', ['disable-popup-blocking', 'enable-automation'])  # Disable popup
    options.add_argument("window-size=500, 500")  # Set window size
    options.add_argument("incognito")  # Secret mode
    # options.add_argument("--headless") # Run in background
    options.add_argument("--mute-audio")  # Mute audio
    options.add_argument(f"user-agent={user_info}")

    new_driver = webdriver.Chrome(options=options, service=service)
    return new_driver


def main(driver):
    url = "https://m2.melon.com/index.htm"
    driver.get(url)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "img.img-logo").click()
    time.sleep(3)
    song_info = {}

    nav_items = driver.find_elements(By.CSS_SELECTOR, "li.nav_item a")
    for nav_item in nav_items:
        if nav_item.text == '멜론차트':
            nav_item.click()
    time.sleep(3)

    for i in range(5):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    more_info_buttons = driver.find_elements(By.CLASS_NAME, "service_list_more")
    for more_info_button in more_info_buttons:
        if more_info_button.get_attribute("onclick") == "hasMore2();":
            more_info_button.click()
    time.sleep(3)

    song_list = driver.find_element(By.CSS_SELECTOR, "ul.list_music")
    songs = song_list.find_elements(By.CSS_SELECTOR, "li.list_item")
    for song in songs:
        song_name = song.find_element(By.CSS_SELECTOR, "p.title").text.strip()
        song_rank = song.find_element(By.CSS_SELECTOR, "div.ranking_num").text.strip().replace('\n', '')
        singer_name = song.find_element(By.CSS_SELECTOR, "span.name").text.strip()

        song_info[f'{song_name}'] = {
            'rank': song_rank,
            'singer': singer_name
        }

    for el in song_info.items():
        print(el)


if __name__ == "__main__":
    driver = init_driver()
    main(driver)
