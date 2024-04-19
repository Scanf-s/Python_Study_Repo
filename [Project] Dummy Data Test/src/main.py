import os
import platform
import sys

from faker import Faker
from faker_airtravel import AirTravelProvider
from sqlalchemy import create_engine, MetaData, delete, text

from dummy_generator import (airline_generator,
                             airport_generator,
                             airplane_type_generator,
                             airplane_generator,
                             airport_geo_generator,
                             airport_reachable_generator,
                             booking_generator,
                             employee_generator,
                             flight_log_generator,
                             flightschedule_generator,
                             flight_generator,
                             passenger_generator,
                             passengerdetails_generator,
                             weatherdata_generator)


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
def insert_dummy_data(engine, table_name, dummy_data, mode):
    try:
        table = get_table_metadata(engine, table_name)
        # DB에서 테이블 원형 가져오기
        if table_name == 'airline':
            # 가져온 table에 fake dummy data 삽입
            with engine.connect() as connection:
                # INSERT전, 모든 테이블 데이터 삭제
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "iata": data[0],
                        "airlinename": data[1],
                        "base_airport": data[2]})
                connection.commit()
        elif table_name == 'airport':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "iata": data[0],
                        "icao": data[1],
                        "name": data[2]
                    })
                connection.commit()
        elif table_name == 'airplane_type':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "identifier": data[0],
                        "description": data[1]
                    })
                connection.commit()
        elif table_name == 'airplane':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "capacity": data[0],
                        "type_id": data[1],
                        "airline_id": data[2]
                    })
                connection.commit()
        elif table_name == 'airport_geo':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "airport_id": data[0],
                        "name": data[1],
                        "city": data[2],
                        "country": data[3],
                        "latitude": data[4],
                        "longitude": data[5],
                    })
                connection.commit()
        elif table_name == 'airport_reachable':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "airport_id": data[0],
                        "hops": data[1]
                    })
                connection.commit()
        elif table_name == 'booking':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "flight_id": data[0],
                        "seat": data[1],
                        "passenger_id": data[2],
                        "price": data[3],
                    })
                connection.commit()
        elif table_name == 'employee':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "firstname": data[0],
                        "lastname": data[1],
                        "birthdate": data[2],
                        "sex": data[3],
                        "street": data[4],
                        "city": data[5],
                        "zip": data[6],
                        "country": data[7],
                        "emailaddress": data[8],
                        "telephoneno": data[9],
                        "salary": data[10],
                        "department": data[11],
                        "username": data[12],
                        "password": data[13]
                    })
                connection.commit()
        elif table_name == 'flight_log':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "log_date": data[0],
                        "user": data[1],
                        "flight_id": data[2],
                        "flightno_old": data[3],
                        "flightno_new": data[4],
                        "from_old": data[5],
                        "to_old": data[6],
                        "from_new": data[7],
                        "to_new": data[8],
                        "departure_old": data[9],
                        "arrival_old": data[10],
                        "departure_new": data[11],
                        "arrival_new": data[12],
                        "airplane_id_old": data[13],
                        "airplane_id_new": data[14],
                        "airline_id_old": data[15],
                        "airline_id_new": data[16],
                        "comment": data[17]
                    })
                connection.commit()
        elif table_name == 'flightschedule':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "flightno": data[0],
                        "from": data[1],
                        "to": data[2],
                        "departure": data[3],
                        "arrival": data[4],
                        "airline_id": data[5],
                        "monday": data[6],
                        "tuesday": data[7],
                        "wednesday": data[8],
                        "thursday": data[9],
                        "friday": data[10],
                        "saturday": data[11],
                        "sunday": data[12]
                    })
                connection.commit()
        elif table_name == 'flight':
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "flightno": data[0],
                        "from": data[1],
                        "to": data[2],
                        "departure": data[3],
                        "arrival": data[4],
                        "airline_id": data[5],
                        "airplane_id": data[6]
                    })
                connection.commit()
        elif table_name == "passenger":
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "passportno": data[0],
                        "firstname": data[1],
                        "lastname": data[2]
                    })
                connection.commit()
        elif table_name == "passengerdetails":
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "passenger_id": data[0],
                        "birthdate": data[1],
                        "sex": data[2],
                        "street": data[3],
                        "city": data[4],
                        "zip": data[5],
                        "country": data[6],
                        "emailaddress": data[7],
                        "telephoneno": data[8]
                    })
                connection.commit()
        elif table_name == "weatherdata":
            with engine.connect() as connection:
                if mode == 'y' or mode == 'Y':
                    delete_current_data(connection, table)
                for data in dummy_data:
                    connection.execute(table.insert(), {
                        "log_date": data[0],
                        "time": data[1],
                        "station": data[2],
                        "temp": data[3],
                        "humidity": data[4],
                        "airpressure": data[5],
                        "wind": data[6],
                        "weather": data[7],
                        "winddirection": data[8]
                    })
                connection.commit()
    except Exception as e:
        print(f"ERROR: {e}")


# 테이블 메타데이터 (DB에 저장되어 있는 테이블 원형?) 가져와주는 함수
def get_table_metadata(engine, table_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[table_name]
    return table


# 테이블 출력 해주는 함수
def print_table(engine, table_name):
    table = get_table_metadata(engine, table_name)
    # https://stackoverflow.com/questions/58658690/retrieve-query-results-as-dict-in-sqlalchemy
    with engine.connect() as connection:
        sql = text("SELECT * FROM " + table_name)
        result = connection.execute(sql)
        conv_result = result.mappings().all()
        print(f'\n<<<<<<<<<<<<<<<<<<<<<<<<<<< {table_name} 더미데이터 내역 >>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
        for dic in conv_result:
            print(dic)


# 콘솔 지우는 함수
def clean_console():
    if platform.system() == "Windows":
        os.system('cls')  # for Windows
    else:
        os.system('clear')  # for Linux and MacOS


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
        try:
            clean_console()
            print("\n더미 데이터 생성 프로그램\n1. 더미 데이터 생성\n2. 테스트 데이터 확인\n3. 종료")
            choice = input("메뉴 입력: ")

            # 더미 데이터 생성
            if choice == '1':
                clean_console()
                num_records = int(input("얼마나 생성할까요?: "))
                mode = input("테이블을 초기화하고 새로 입력하시겠습니까? [y/n]: ")
                if not (mode == 'y' or mode == 'Y' or mode == 'n' or mode == 'N'):
                    raise ValueError("유효하지 않은 모드 선택: 모드는 'y/Y' 또는 'n/N' 이어야 합니다.")
                table_name = input("테이블 이름을 정확히 입력해주세요: ")

                # 존재하지 않는 테이블을 가져왔다면
                if table_name not in table_lists:
                    raise ValueError(f"테이블 이름 '{table_name}'은(는) 유효하지 않습니다. 가능한 테이블 이름을 확인해주세요.")
                else:
                    try:
                        if table_name == 'airline':
                            dummy_data = airline_generator.generate_airline_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airport':
                            dummy_data = airport_generator.generate_airport_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airplane_type':
                            dummy_data = airplane_type_generator.generate_airplane_type_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airplane':
                            dummy_data = airplane_generator.generate_airplane_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airport_geo':
                            dummy_data = airport_geo_generator.generate_airport_geo_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airport_reachable':
                            dummy_data = airport_reachable_generator.generate_airport_reachable_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'booking':
                            dummy_data = booking_generator.generate_booking_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'employee':
                            dummy_data = employee_generator.generate_employee_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'flight_log':
                            dummy_data = flight_log_generator.generate_flight_log_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'flightschedule':
                            dummy_data = flightschedule_generator.generate_flightschedule_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'flight':
                            dummy_data = flight_generator.generate_flight_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'passenger':
                            dummy_data = passenger_generator.generate_passenger_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'passengerdetails':
                            dummy_data = passengerdetails_generator.generate_passengerdetails_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'weatherdata':
                            dummy_data = weatherdata_generator.generate_weatherdata_dummy_data(fake, num_records)
                            insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        else:
                            print("올바른 테이블명을 입력해주세요.")
                    except ValueError as ve:
                        print(f"입력 오류: {ve}")
                    except Exception as e:
                        print("Exception Occurs : ", e)

            # 테스트 데이터 출력
            elif choice == '2':
                clean_console()
                table_name = input("테이블 이름을 정확히 입력해주세요: ")
                # 존재하지 않는 테이블을 가져왔다면
                if table_name not in table_lists:
                    print("테이블 이름이 정확하지 않습니다")
                else:
                    print_table(engine, table_name)

            elif choice == '3':
                clean_console()
                sys.exit(0)
            else:
                print("다시 입력해주세요.")
        except KeyboardInterrupt as ki:
            print(f"사용자 임의 종료")
            sys.exit(0)

if __name__ == "__main__":
    main()
