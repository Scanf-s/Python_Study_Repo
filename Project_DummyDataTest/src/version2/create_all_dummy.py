import random
import re
import traceback

from Project_DummyDataTest.src import table_modifier


def generator(fake, table, n):
    dummy_data = []
    for i in range(n):  # n개의 더미 데이터 생성
        check_duplicate = set()
        data_row = {}
        for column in table.columns:
            if str(column.autoincrement) == "True":
                continue
            type_detail = get_column_type_detail(table, column)
            data_row[column.name] = generate_data(fake, type_detail, check_duplicate)
        dummy_data.append(data_row)
    return dummy_data


# 해당 COL의 모든 CONSTRAINT및 잡다한 정보를 가져와주는 함수
def get_column_type_detail(table, column):
    column_type = column.type
    pattern = r"(\w+)\s*(\((\d+)(,\s*(\d+))?\))?(?:\s*CHARACTER SET \w+)?(?:\s*COLLATE \w+)?"  # 정규식 (CHAT-GPT 사용)
    matches = re.findall(pattern, str(column_type))
    type_detail = {
        'table_name': table.name,
        'col_name': column.name,
        'type': None,
        'size': None,
        'decimal_place': None,
        'enum_values': None,
        'primary': None,
        'unique': None
    }

    if matches:
        col_type, col_size, decimal_place = matches[0][0], matches[0][2], matches[0][4]
        type_detail['type'] = col_type
        type_detail['size'] = int(col_size) if col_size else None
        type_detail['decimal_place'] = int(decimal_place) if decimal_place else None

    # primary
    if column.primary_key:
        type_detail['primary'] = 'True'

    # 유니크 속성 확인
    for index in table.indexes:
        if index.unique and column.name in index.columns:
            type_detail['unique'] = 'True'
            break

    # ENUM 값 뽑아오기
    if str(column_type) == "ENUM":
        type_detail['enum_values'] = column_type.enums

    return type_detail


def generate_data(fake, type_detail, check_duplicate):
    try:
        data_type = type_detail['type']
        size = type_detail['size']
        decimal_place = type_detail.get('decimal_place')

        if data_type in ["INTEGER", "SMALLINT", "MEDIUMINT", "TINYINT"]:
            if type_detail.get('primary') == 'True' or type_detail.get('unique') == 'True':
                generated_int = random.randint(1, 20001) if data_type != "TINYINT" else random.randint(0, 2)
                while str(generated_int) in check_duplicate:
                    generated_int = random.randint(1, 20001) if data_type != "TINYINT" else random.randint(0, 2)
                check_duplicate.add(str(generated_int))
                return generated_int
            else:
                return random.randint(1, 20001) if data_type != "TINYINT" else random.randint(0, 2)

        elif data_type in ["CHAR", "VARCHAR", "TEXT"]:
            if data_type == "CHAR" and size:  # char
                if type_detail.get('primary') == 'True' or type_detail.get('unique') == 'True':
                    # 알파벳 문자만으로 생성하면 최대 676개까지의 ROW밖에 생성할 수 없기 때문에
                    # 다른 문자도 섞어서 해줘야한다.
                    # 추후 수정 예정입니다.
                    distinct_chars = ''.join(chr(i) for i in range(32, 127))
                    generated_char = fake.lexify('?' * size, letters=distinct_chars)
                    while generated_char in check_duplicate:
                        generated_char = fake.lexify('?' * size, letters=distinct_chars)
                    check_duplicate.add(generated_char)
                    return generated_char
                else:
                    return fake.lexify('?' * size, letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            elif size:  # varchar
                return fake.text(max_nb_chars=size)
            else:  # text
                return fake.text()

        elif data_type in ["DECIMAL"]:
            if size and decimal_place:
                max_value = 10 ** (size - decimal_place) - 1
                return round(random.uniform(0, max_value), decimal_place)
            else:
                return round(random.uniform(0, 10000), 2)

        elif data_type in ["DATE"]:
            return fake.date()

        elif data_type in ["TIME"]:
            return fake.time()

        elif data_type in ["DATETIME"]:
            return fake.date_time()

        elif data_type in ["ENUM"]:
            if 'enum_values' in type_detail:
                return random.choice(type_detail['enum_values'])
            else:
                return None

        else:
            return None
    except Exception:
        traceback.print_exc()


def run(engine, fake, n, mode):
    table_list = table_modifier.get_all_tables_from_database(engine)
    all_dummy_data = {}
    for table in table_list:
        meta_table = table_modifier.get_table_metadata(engine, table)
        generated_data = generator(fake, meta_table, n)
        all_dummy_data[meta_table.name] = generated_data
    table_modifier.insert_into_all_tables(engine, all_dummy_data, mode)
