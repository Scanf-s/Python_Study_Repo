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

## 사용해야할 라이브러리
- [X] sqlalchemy : https://www.sqlalchemy.org/
- [X] Faker : https://faker.readthedocs.io/en/master/

## 해보면 좋은 것 (안해도 상관없는 것)
- [] 패키지관리자로 poetry 사용해보기


## 유의사항
이번 프로젝트는 첫번째 프로젝트인 만큼 현재 상태를 알기위한 목적이라 할수 있는 만큼 만 구현해주시면 됩니다.

faker, sqlalchemy 같이 처음 접하는 라이브러리라도 사용법을 찾아서 적용해보는 연습을 하는 시간이라고 생각해주시면됩니다. 
사용법을 찾아서 적용하기 어려워도 괜찮습니다. 어려운게 당연합니다.

https://www.sqlalchemy.org/
