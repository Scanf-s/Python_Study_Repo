import os
import platform
import sys

from faker import Faker
from faker_airtravel import AirTravelProvider
from sqlalchemy import create_engine, MetaData, delete, text

from dummy_generator import airline_generator, airport_generator


# 데이터베이스 연결 함수
def create_connection():
    try:
        engine = create_engine('mysql+pymysql://root:123123@localhost:3306/airportdb?charset=utf8mb4', echo=True)
        return engine
    except Exception as e:
        print(f"ERROR: {e}")


# 테이블 데이터 삭제(초기화) 함수
def delete_current_data(connection, table):
    connection.execute(delete(table))
    connection.commit()


# 테이블 데이터 삽입 함수
def insert_dummy_data(engine, table_name, dummy_data):
    # DB에서 테이블 원형 가져오기
    if table_name == 'airline':
        table = get_table_metadata(engine, table_name)
        # 가져온 table에 fake dummy data 삽입
        with engine.connect() as connection:
            # INSERT전, 모든 테이블 데이터 삭제
            delete_current_data(connection, table)
            for data in dummy_data:
                connection.execute(table.insert(), {
                    "airline_id": data[0],
                    "iata": data[1],
                    "airlinename": data[2],
                    "base_airport": data[3]})
            connection.commit()
    elif table_name == 'airport':
        table = get_table_metadata(engine, table_name)
        with engine.connect() as connection:
            delete_current_data(connection, table)
            for data in dummy_data:
                connection.execute(table.insert(), {
                    "airport_id": data[0],
                    "iata": data[1],
                    "icao": data[2],
                    "name": data[3]
                })
            connection.commit()
    else:
        print("미구현 입니다.")


# 테이블 메타데이터 (DB에 저장되어 있는 테이블 원형?) 가져와주는 함수
def get_table_metadata(engine, table_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[table_name]
    return table


# 콘솔 지워주는 함수
def clean_console():
    if platform.system() == "Windows":
        os.system('cls')  # for Windows
    else:
        os.system('clear')  # for Linux and MacOS


def result_dict(r):
    return dict(zip(r.keys(), r))


def result_dicts(rs):
    return list(map(result_dict, rs))


# main
def main():
    engine = create_connection()
    fake = Faker()
    fake.add_provider(AirTravelProvider)

    # DB에 저장된 테이블 이름 목록 검증을 위한 리스트
    table_lists = [
        'airline',
        'airplane',
        'airplane_type',
        'airport',
        'airport_geo',
        'airport_reachable',
        'booking',
        'employee',
        'flight',
        'flight_log',
        'flightschedule',
        'passenger',
        'passengerdetails',
        'weatherdata'
    ]

    while True:
        clean_console()
        print("\n더미 데이터 생성 프로그램\n1. 더미 데이터 생성\n2. 테스트 데이터 확인\n3. 종료")
        choice = input("Enter choice: ")

        # 더미 데이터 생성
        if choice == '1':
            num_records = int(input("얼마나 생성할까요?: "))
            table_name = input("테이블 이름을 정확히 입력해주세요: ")

            # 존재하지 않는 테이블을 가져왔다면
            if table_name not in table_lists:
                print("테이블 이름이 정확하지 않습니다")
            else:
                if table_name == 'airline':
                    dummy_data = airline_generator.generate_airline_dummy_data(fake, num_records)
                    insert_dummy_data(engine, "airline", dummy_data)
                    print("Data inserted successfully!")
                elif table_name == 'airport':
                    dummy_data = airport_generator.generate_airport_dummy_data(fake, num_records)
                    insert_dummy_data(engine, "airport", dummy_data)
                    print("Data inserted successfully!")
                else:
                    print("미구현 입니다.")

        # 테스트 데이터 출력
        elif choice == '2':
            table_name = input("테이블 이름을 정확히 입력해주세요: ")
            # 존재하지 않는 테이블을 가져왔다면
            if table_name not in table_lists:
                print("테이블 이름이 정확하지 않습니다")
            else:
                table = get_table_metadata(engine, table_name)
                # https://stackoverflow.com/questions/58658690/retrieve-query-results-as-dict-in-sqlalchemy
                with engine.connect() as connection:
                    sql = text("SELECT * FROM " + table_name)
                    result = connection.execute(sql)
                    conv_result = result.mappings().all()
                    print(f'\n<<<<<<<<<<<<<<<<<<<<<<<<<<< {table_name} 더미데이터 내역 >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
                    for dic in conv_result:
                        print(dic)

        elif choice == '3':
            sys.exit(0)
        else:
            print("다시 입력해주세요.")


if __name__ == "__main__":
    main()
