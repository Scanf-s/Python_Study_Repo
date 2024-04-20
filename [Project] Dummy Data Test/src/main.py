import os
import platform
import sys

from faker import Faker
from faker_airtravel import AirTravelProvider
from sqlalchemy import create_engine
import table_modifier

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
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airport':
                            dummy_data = airport_generator.generate_airport_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airplane_type':
                            dummy_data = airplane_type_generator.generate_airplane_type_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airplane':
                            dummy_data = airplane_generator.generate_airplane_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airport_geo':
                            dummy_data = airport_geo_generator.generate_airport_geo_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'airport_reachable':
                            dummy_data = airport_reachable_generator.generate_airport_reachable_dummy_data(fake,
                                                                                                           num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'booking':
                            dummy_data = booking_generator.generate_booking_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'employee':
                            dummy_data = employee_generator.generate_employee_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'flight_log':
                            dummy_data = flight_log_generator.generate_flight_log_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'flightschedule':
                            dummy_data = flightschedule_generator.generate_flightschedule_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'flight':
                            dummy_data = flight_generator.generate_flight_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'passenger':
                            dummy_data = passenger_generator.generate_passenger_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'passengerdetails':
                            dummy_data = passengerdetails_generator.generate_passengerdetails_dummy_data(fake,
                                                                                                         num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
                            print("데이터를 정상적으로 적용했습니다.")
                        elif table_name == 'weatherdata':
                            dummy_data = weatherdata_generator.generate_weatherdata_dummy_data(fake, num_records)
                            table_modifier.insert_dummy_data(engine, table_name, dummy_data, mode)
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
                    table_modifier.print_table(engine, table_name)

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
