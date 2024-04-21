from sqlalchemy import MetaData, delete, text


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


# 테이블 데이터 삭제(초기화) 함수
def delete_current_data(connection, table):
    connection.execute(delete(table))
    connection.commit()


# 테이블 메타데이터 (DB에 저장되어 있는 테이블 원형?) 가져와주는 함수
def get_table_metadata(engine, table_name):
    metadata = MetaData()
    metadata.reflect(bind=engine)
    table = metadata.tables[table_name]
    return table


# 더미 데이터 삽입 함수
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
