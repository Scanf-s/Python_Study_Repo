# 2주차 과제 : 4월24일~5월1일

## 주제 : 테스트를 위한 dummy 데이터 만들기 2차 (MySQL)

## 상황
- 1차로 만들어준 더미데이터가 유용했다면서, 새로운 MySQL 데이터베이스(스키마)에 테스트용 데이터를 채워줄 것을 요청받음
- 이번에도 새로운 Table이 10개 만들어져있음.
- 나머지 요건은 지난번과 같음.

## 가이드
- 반복되는 똑같은 행위를 2번 해야한다.
- 1차때처럼 테이블 단위로 칼럼별로 하드코딩하는 형태로 대응하면 계속 수정해야한다.
- ``테스트 데이터를 생성하는 코드를 완전 공통화 해보는건 어떨까?``
ex) AUTO_INCREMENT 칼럼은 대상칼럼에서 제거

## 이제 해볼것
poetry 사용하기
파이썬 실행환경은 너무 다양하다.
global 환경에서 실행할수도있고, virtualenv를 직접세팅해서 쓸수도, conda를 쓸수도있고, colab에서 개발하수도있고 천차만별.
자바, 자바스크립트 개발자로서 파이썬을 경험하면서 가장 맘에 들었던  패키지관리도구이고, 가장 최신의 poetry를 기반으로 환경을 세팅해보자

## 제출방식
작성한 Github 주소 공유

## 유의사항
아마존은 같은일을 3번 반복하면 자동화한다고 합니다.
파이썬만큼 빠르게 작성하고 실행할수있는 좋은 도구가 많지않습니다.
당장 눈앞의 과제를 해결하는 것도 좋은데, 같은일이 반복될거같으면 공통화 해보세요.

## 이번 과제의 목적
테스트 데이터를 매번 세팅하는 일은 아주 번거롭습니다. 더미데이터를 세팅하는 프로그램은 한번 잘 만들어 두면, 실무에서 두고두고 써먹을 수 있는 아주 좋은 도구입니다.
이 로직을 잘 정리해서 추후에 배울 서버 API 요청에서 호출하도록하면, 지정한 데이터베이스의 테이블에 더미데이터를 생성해주는 백엔드 API를 만들게 되는 것입니다. 사내 어드민 도구에서 버튼 클릭으로 제어하게 할수 있는겁니다.

<br>
<br>
<br>

---

<br>
<br>
<br>

# 1주차 과제 : 4월17일~4월24일

## 주제

> 테스트를 위한 dummy 데이터 만들기 (MySQL)

## 상황
- [X] MySQL의 Database에 14개의 테이블을 생성함.
- [X] Table만 만든 상태라서 테스트를 위해 더미데이터를 테이블 별로 1000개~2만개 사이로 세팅해달라는 요청을 받음
- [X] 테이블 별로 데이터를 몇 건 씩 세팅할지 지정할 수 있어야함.
- [X] 더미데이터 생성시마다 데이터를 전부 삭제하고 새로 세팅할지, 추가할지를 지정할 수 있어야함.

## 가이드 (힌트)
- [X] sqlalchemy의 MetaData()를 이용하세요. metadata.reflect() 을 이용하면 현재 접속한 database의 table, column 정보를 얻을 수 있습니다.

## Libraries
- [X] [SQLAlchemy 라이브러리 링크](https://www.sqlalchemy.org/)
- [X] [Faker 라이브러리 링크](https://faker.readthedocs.io/en/master/)

## 해보면 좋은 것 (안해도 상관없는 것)
- [ ] 패키지관리자로 poetry 사용해보기


## 유의 사항
이번 프로젝트는 첫번째 프로젝트인 만큼 현재 상태를 알기위한 목적이라 할수 있는 만큼 만 구현해주시면 됩니다.

faker, sqlalchemy 같이 처음 접하는 라이브러리라도 사용법을 찾아서 적용해보는 연습을 하는 시간이라고 생각해주시면됩니다. 
사용법을 찾아서 적용하기 어려워도 괜찮습니다. 어려운게 당연합니다.

[SQLAlchemy 라이브러리 링크](https://www.sqlalchemy.org/)

## Instructions
1. Clone the project into your local repository.

2. Start MySQL, and then use the **`airport-ddl.sql`** script located in the MySQL/DDL directory of the project to create the database and tables.

3. Execute the **`main.py`** file to run the project.

## 프로젝트 구조
```yaml
[Project] Dummy Data Test
│  readme.md
│
├─MySQL
│  └─DDL
│          airport-ddl.sql
│
└─src
    │  main.py
    │  table_modifier.py
    │
    └─dummy_generator
        │  airline_generator.py
        │  airplane_generator.py
        │  airplane_type_generator.py
        │  airport_generator.py
        │  airport_geo_generator.py
        │  airport_reachable_generator.py
        │  booking_generator.py
        │  employee_generator.py
        │  flightschedule_generator.py
        │  flight_generator.py
        │  flight_log_generator.py
        │  passengerdetails_generator.py
        │  passenger_generator.py
        │  weatherdata_generator.py
        │
        └─__pycache__
                airline_generator.cpython-312.pyc
                airplane_generator.cpython-312.pyc
                airplane_type_generator.cpython-312.pyc
                airport_generator.cpython-312.pyc
                airport_geo_generator.cpython-312.pyc
                airport_reachable_generator.cpython-312.pyc
                booking_generator.cpython-312.pyc
                employee_generator.cpython-312.pyc
                flightschedule_generator.cpython-312.pyc
                flight_generator.cpython-312.pyc
                flight_log_generator.cpython-312.pyc
                passengerdetails_generator.cpython-312.pyc
                passenger_generator.cpython-312.pyc
                weatherdata_generator.cpython-312.pyc
```
