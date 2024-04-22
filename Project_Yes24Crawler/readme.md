# YES24 베스트셀러 스크래퍼
이 프로젝트는 YES24의 베스트셀러 목록에서 책의 상세 정보를 스크래핑하여 데이터베이스에 저장하는 파이썬 스크립트입니다. 
Selenium과 SQLAlchemy를 활용하여 웹 페이지의 정보를 추출하고, 
MySQL 데이터베이스에 책의 제목, 저자, 출판사, 출판일, 평점, 리뷰 수, 판매 순위, 가격, 순위, 순위 유지 기간을 저장합니다.

# 주요 기능
- 데이터 추출: 웹 드라이버를 사용하여 YES24 베스트셀러 페이지에서 책 링크를 추출합니다.
- 상세 정보 스크래핑: 각 책의 상세 페이지로부터 필요한 정보를 추출합니다.
- 데이터 저장: 추출한 데이터를 MySQL 데이터베이스에 저장합니다.

# 사용 기술
- Python 3.8 이상
- Selenium: 웹 페이지의 동적 내용을 스크래핑합니다.
- SQLAlchemy: Python에서 SQL 데이터베이스를 쉽게 다루기 위한 라이브러리입니다.
- pymysql: Python에서 MySQL 데이터베이스를 다루기 위한 라이브러리입니다.
- WebDriver Manager: Selenium 웹 드라이버의 자동 관리를 도와줍니다.

# 설치 방법
먼저 프로젝트를 자신의 로컬 드라이브로 clone합니다.
이 스크립트를 실행하기 전에 필요한 라이브러리들을 설치해야 합니다. 
다음 명령어를 사용하여 필요한 라이브러리를 설치할 수 있습니다:
```bash
pip install selenium sqlalchemy pymysql webdriver-manager
```

# 사용법
스크립트를 실행하기 전에 MySQL 데이터베이스에 yes24 데이터베이스와 적절한 테이블을 생성해야 합니다.
MySQL을 열고 다음 쿼리를 실행하세요:
```sql
CREATE TABLE Books (
    bookID INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255),
    publisher VARCHAR(255),
    publishing DATE,
    rating DECIMAL(3, 1),
    review INT,
    sales INT,
    price DECIMAL(10, 2),
    ranking INT,
    ranking_weeks INT
);
```

마지막으로, 다음 명령어로 파이썬 스크립트를 실행하세요:
```bash
python yes24_scraper.py
```
스크립트 실행 중, 스크래핑할 페이지 수를 입력하면 됩니다.

# 주의 사항
이 스크립트는 YES24 웹사이트의 구조 변경에 따라 작동하지 않을 수 있습니다.
