import datetime
from datetime import datetime

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from sqlalchemy import create_engine, MetaData
from webdriver_manager.chrome import ChromeDriverManager


def create_connection():
    try:
        engine = create_engine('mysql+pymysql://root:123123@localhost:3306/yes24?charset=utf8mb4', echo=True)
        return engine
    except Exception as e:
        print(f"ERROR: {e}")


def get_table_metadata(engine):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    return metadata.tables['books']


def scrape_page_links(browser, url):
    browser.get(url)
    return [link.get_attribute('href') for link in browser.find_elements(By.CLASS_NAME, 'gd_name')]


def scrape_book_details(browser, link):
    try:
        browser.get(link)
        try:
            title = browser.find_element(By.CLASS_NAME, 'gd_name').text
        except NoSuchElementException:
            title = None
        except IndexError:
            title = None

        try:
            author = browser.find_element(By.CLASS_NAME, 'gd_auth').text
        except NoSuchElementException:
            author = None
        except IndexError:
            author = None

        try:
            publisher = browser.find_element(By.CLASS_NAME, 'gd_pub').text
        except NoSuchElementException:
            publisher = None
        except IndexError:
            publisher = None

        try:
            date = browser.find_element(By.CLASS_NAME, 'gd_date').text
            if date:
                date_obj = datetime.strptime(date, '%Y년 %m월 %d일')
                date = date_obj.strftime('%Y-%m-%d')
        except NoSuchElementException:
            date = None
        except IndexError:
            date = None

        try:
            rating = browser.find_element(By.CLASS_NAME, 'gd_rating').find_element(By.CLASS_NAME, 'yes_b').text
        except NoSuchElementException:
            rating = None
        except IndexError:
            rating = None

        try:
            review_amount = browser.find_element(By.CLASS_NAME, 'gd_reviewCount').find_element(By.CLASS_NAME,
                                                                                               'txC_blue').text
            temps = review_amount.split(',')
            review_temp = ""
            for temp in temps:
                review_temp += temp
            review_amount = review_temp
        except NoSuchElementException:
            review_amount = None
        except IndexError:
            review_amount = None

        try:
            sales_index = browser.find_element(By.CLASS_NAME, 'gd_sellNum').text.split(" ")[2]
            temps = sales_index.split(",")
            sales_temp = ""
            for temp in temps:
                sales_temp += temp
            sales_index = sales_temp
        except NoSuchElementException:
            sales_index = None
        except IndexError:
            sales_index = None

        try:
            price = browser.find_element(By.CLASS_NAME, 'yes_m').text[:-1]
            temps = price.split(",")
            int_price = ""
            for temp in temps:
                int_price += temp
            price = int_price
        except NoSuchElementException:
            price = None
        except IndexError:
            price = None

        try:
            ranking = browser.find_element(By.CLASS_NAME, 'gd_best ').text.split(" | ")[0].split(" ")[-1][:-1]
        except NoSuchElementException:
            ranking = None
        except IndexError:
            ranking = None

        try:
            ranking_weeks = browser.find_element(By.CLASS_NAME, 'gd_best').text.split(" | ")[1].split(" ")[-1][:-1]
        except NoSuchElementException:
            ranking_weeks = None
        except IndexError:
            ranking_weeks = None

        return title, author, publisher, date, rating, review_amount, sales_index, price, ranking, ranking_weeks

    except Exception as e:
        print(f"ERROR: {e}")


def insert_details(engine, table, details):
    try:
        with engine.connect() as connection:
            for detail in details:
                connection.execute(table.insert(), {
                    "title": detail[0],
                    "author": detail[1],
                    "publisher": detail[2],
                    "publishing": detail[3],
                    "rating": detail[4],
                    "review": detail[5],
                    "sales": detail[6],
                    "price": detail[7],
                    "ranking": detail[8],
                    "ranking_weeks": detail[9]
                })
            connection.commit()

    except Exception as e:
        print(f"ERROR: {e}")


if __name__ == '__main__':
    engine = create_connection()
    table = get_table_metadata(engine)
    ChromeDriverManager().install()
    browser = webdriver.Chrome()

    n = int(input("Enter number of pages: "))
    details = []

    for cnt in range(n):
        print(f'\nScraping page {cnt + 1}\n')
        url = f'https://www.yes24.com/Product/Category/BestSeller?categoryNumber=001&pageNumber={cnt + 1}&pageSize=24'
        page_links = scrape_page_links(browser, url)

        for link in page_links:
            book_details = scrape_book_details(browser, link)

            if book_details is not None:
                details.append(book_details)
            print(book_details)

    browser.quit()

    insert_details(engine, table, details)
