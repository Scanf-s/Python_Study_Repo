from pymongo import MongoClient
from datetime import datetime, timezone

def insert_data():
    # 책 데이터 삽입
    books = [
        {"title": "Kafka on the Shore", "author": "Haruki Murakami", "year": 2002, "genre": "Fiction"},
        {"title": "Norwegian Wood", "author": "Haruki Murakami", "year": 1987, "genre": "Fiction"},
        {"title": "1Q84", "author": "Haruki Murakami", "year": 2009, "genre": "Fiction"},
        {"title": "123123", "author": "asdf", "year": 2011, "genre": "asdf"},
        {"title": "3453453", "author": "asdf", "year": 2013, "genre": "asdf"},
        {"title": "4564567", "author": "asdf", "year": 2013, "genre": "asdf"},
    ]
    # 이거 전부 집어넣어야하므로 insert_many 함수 사용
    db.books.insert_many(books)

    # 영화 데이터 삽입
    movies = [
        {"title": "Inception", "director": "Christopher Nolan", "year": 2010, "rating": 8.8},
        {"title": "Interstellar", "director": "Christopher Nolan", "year": 2014, "rating": 8.6},
        {"title": "The Dark Knight", "director": "Christopher Nolan", "year": 2008, "rating": 9.0},
        {"title": "ADASDAD", "director": "Scanf-s", "year": 2008, "rating": 10.0},
        {"title": "123123", "director": "Scanf-s", "year": 2008, "rating": 9.5},
        {"title": "343434", "director": "Scanf-s", "year": 2008, "rating": 7.0},
    ]
    db.movies.insert_many(movies)

    # 사용자 행동 데이터 삽입
    user_actions = [
        {"user_id": 1, "action": "click", "timestamp": "2023-04-12T08:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-12T09:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T10:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T11:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T12:00:00Z"},
        {"user_id": 2, "action": "purchase", "timestamp": "2023-04-12T13:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-09T13:00:00Z"},
        {"user_id": 1, "action": "view", "timestamp": "2023-04-09T13:00:00Z"},
    ]
    db.user_actions.insert_many(user_actions)

    print("Data inserted successfully")


def question1(db, genre):
    # books 컬렉션 db로부터 가져오기
    books = db.books

    find_books = books.find({"genre": genre}, {})
    for book in find_books:
        print(book)


def question2(db):
    # https://www.mongodb.com/docs/manual/reference/operator/aggregation/sort/
    movies = db.movies
    avg_by_director = movies.aggregate([
        {
            "$group": {"_id": "$director", "avg": {"$avg": "$rating"}}
        },
        {
            "$sort": {"avg": -1}
        }
    ])

    for director in avg_by_director:
        print(director)


def question3(db, user_id):
    # https://www.mongodb.com/docs/manual/reference/method/cursor.sort/
    user_actions = db.user_actions
    recent_behavior = user_actions.find({"user_id": user_id}).sort("timestamp", -1)
    for behavior in recent_behavior:
        print(behavior)


def question4(db):
    # https://www.mongodb.com/docs/manual/reference/operator/aggregation/sum/
    books_collection = db.books

    results = books_collection.aggregate([
        {
            "$group": {"_id": "$year", "count": {"$sum": 1}}
        },
        {
            "$sort": {"count": -1}
        }
    ])
    for result in results:
        print(result)


def question5(db, user_id, date):
    user_actions = db.user_actions
    user_actions.update_many(
        # 1번 중괄호에 해당하는 모든 사용자 행동 데이터를 가져와서
        {
            "user_id": user_id,
            # 그냥 date만 집어넣어서 비교하면 제대로 비교하지 않음.
            # .isoformat()함수를 사용하여 형식에 맞게 date를 변형하여 less than 비교 수행
            "timestamp": {"$lt": date.isoformat()},
            "action": "view"
        },
        # 그 사용자 행동 데이터의 "action"을 seen으로 변경
        {
            "$set": {"action": "seen"}
        }
    )

    for user_action in user_actions.find({}):
        print(user_action)


if __name__ == "__main__":
    # init
    client = MongoClient('mongodb://localhost:27017/')
    db = client.local  # 'local' 데이터베이스 사용
    insert_data()

    # 1. 특정 장르의 책 찾기
    """
        - **문제 설명**:
        데이터베이스에 새로운 필드로 **`genre`**를 책 데이터에 추가하였습니다. 
        사용자는 "fantasy" 장르의 모든 책을 찾고 싶어합니다.
        
        - **쿼리 작성 목표**:
        "fantasy" 장르에 해당하는 모든 책의 제목과 
        저자를 찾는 MongoDB 쿼리를 함수로 만들어 문제를 해결해 봅니다.
    """
    question1(db, input("장르 입력 : "))

    # 2. 감독별 평균 영화 평점 계산
    """
        - **문제 설명**:
        각 영화 감독별로 그들의 영화 평점의 평균을 계산하고 싶습니다. 
        이를 통해 어떤 감독이 가장 높은 평균 평점을 가지고 있는지 알아볼 수 있습니다.

        - **쿼리 작성 목표**:
    `   모든 영화 감독의 영화 평점 평균을 계산하고, 
        평균 평점이 높은 순으로 정렬하는 MongoDB 쿼리를 함수로 만들어 문제를 해결해 봅니다.
    """
    question2(db)

    # 3. 특정 사용자의 최근 행동 조회
    """
        - **문제 설명**:
        특정 사용자의 최근 행동 로그를 조회하고자 합니다. 
        이 때, 최신 순으로 정렬하여 최근 5개의 행동만을 보고 싶습니다.
        
        - **쿼리 작성 목표**:
        사용자 ID가 1인 사용자의 최근 행동 5개를 시간 순으로 정렬하여 
        조회하는 MongoDB 쿼리를 함수로 만들어 문제를 해결해 봅니다.
    """
    question3(db, 1)

    # 4. 출판 연도별 책의 수 계산
    """
        - **문제 설명** :
        데이터베이스에 저장된 책 데이터를 이용하여
        각 출판 연도별로 출판된 책의 수를 계산하고자 합니다. 
        이 데이터는 시간에 따른 출판 트렌드를 분석하는 데 사용될 수 있습니다.
        
        - **쿼리 작성 목표** :
        각 출판 연도별로 출판된 책의 수를 계산하고, 
        출판된 책의 수가 많은 순서대로 정렬하는 MongoDB 쿼리를 함수로 만들어 문제를 해결해 봅니다.
    """
    question4(db)

    # 5. 특정 사용자의 행동 유형 업데이트
    """
        - **문제 설명**:
        특정 사용자의 행동 로그 중, 특정 날짜 이전의 "view" 행동을 "seen"으로 변경하고 싶습니다. 
        예를 들어, 사용자 ID가 1인 사용자의 2023년 4월 10일 이전의 
        모든 "view" 행동을 "seen"으로 변경하는 작업입니다.
        
        - **쿼리 작성 목표**:
        사용자 ID가 1인 사용자의 2023년 4월 10일 이전의 "view" 행동을 
        "seen"으로 변경하는 MongoDB 업데이트 쿼리를 함수로 만들어 문제를 해결해 봅니다.
    """
    # "2023-04-09T13:00:00Z"는 MongoDB에서 ISODate Type이다.
    # Python의 datetime을 통해 생성 가능
    question5(db, 1, datetime(2023, 4, 10, 0, 0, 0, tzinfo=timezone.utc))
    client.close()