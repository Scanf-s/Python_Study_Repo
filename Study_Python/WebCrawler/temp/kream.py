import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def init_driver():
    user_info = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
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
    url = "https://kream.co.kr"
    driver.get(url)
    time.sleep(3)  # Wait for page load()
    driver.find_element(By.CSS_SELECTOR, "a.btn_search").click()
    time.sleep(1)
    search_string = input("검색어 입력:")
    driver.find_element(By.CSS_SELECTOR, "div.search input").send_keys("search_string\n")

    for i in range(10):
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

    html = driver.page_source
    print(html)


if __name__ == "__main__":
    driver = init_driver()
    main(driver)
