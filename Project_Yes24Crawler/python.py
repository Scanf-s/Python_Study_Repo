# webdriver-manager
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# selenium
from selenium import webdriver

ChromeDriverManager().install()

browser = webdriver.Chrome()
# url = 'https://www.yes24.com/Product/category/bestseller?CategoryNumber=001&sumgb=06'
# browser.get(url)

# 1페이지의 링크 데이터 전부 수집

# 1개의 링크 수집
# print(browser.find_element(By.CLASS_NAME, 'gd_name').get_attribute('href'))

# 1페이지 전체 링크 데이터 수집
# datas = browser.find_elements(By.CLASS_NAME, 'gd_name')
# for data in datas:
#     print(data.get_attribute('href'))

# n 페이지 전체 링크 데이터 수집
n = int(input("Enter number of pages: "))
yes24_page_links = []
details = []
for cnt in range(n):
    print(f'\n{cnt}번째 페이지 수집\n')
    url = f'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={cnt}&pageSize=24'
    browser.get(url)
    datas = browser.find_elements(By.CLASS_NAME, 'gd_name')
    for data in datas:
        yes24_page_links.append(data.get_attribute('href'))


for link in yes24_page_links:
    # 상세 페이지로 이동
    browser.get(link)
    title = author = publisher = date = rate = review_amount = sales_index = price = ranking = ranking_weeks = None
    # 상세 데이터 가져오기
    try:
        title = browser.find_element(By.CLASS_NAME, 'gd_name').text
        author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
        publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text
        date = browser.find_element(By.CLASS_NAME, 'gd_date').text
        rate = browser.find_element(By.CLASS_NAME, 'gd_rating').find_element(By.TAG_NAME, 'a').find_element(By.TAG_NAME, 'em').text
        review_amount = browser.find_element(By.CLASS_NAME, 'gd_reviewCount').text
        sales_index = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text
        price = browser.find_element(By.CLASS_NAME, 'nor_price').text
        ranking = browser.find_element(By.CLASS_NAME, 'gd_best ').find_element(By.TAG_NAME, 'a').text
        ranking_weeks = browser.find_element(By.CLASS_NAME, 'gd_best').find_element(By.TAG_NAME, 'em').text
    except NoSuchElementException:
        pass

    details.append((title, author, publisher, date, rate, review_amount, sales_index, price, ranking, ranking_weeks))

print(details)