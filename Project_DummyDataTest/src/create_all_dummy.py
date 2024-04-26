from .. import table_modifier
import re, random


def generator(fake, table, n):
    dummy_data = []
    for i in range(n):  # n개의 더미 데이터 생성
        data_row = {}
        for column in table.columns:
            if column.autoincrement:
                continue
            column_type_str = str(column.type)
            type_detail = get_column_type_detail(column_type_str)
            data_row[column.name] = generate_data(fake, type_detail)
        dummy_data.append(data_row)
    return dummy_data


def get_column_type_detail(column_type_str):
    pattern = r"(\w+)(\((\d+)(,\s*(\d+))?\))?"
    matches = re.findall(pattern, column_type_str)
    type_detail = {'type': None, 'size': None, 'decimal_place': None, 'enum_values': None}

    if matches:
        type, size, decimal_place = matches[0][0], matches[0][2], matches[0][4]
        type_detail['type'] = type
        type_detail['size'] = int(size) if size else None
        type_detail['decimal_place'] = int(decimal_place) if decimal_place else None

    # ENUM 값들을 추출하는 부분
    if type_detail['type'] == 'ENUM':
        enum_pattern = r"ENUM\s*\((.*?)\)"
        enum_matches = re.search(enum_pattern, column_type_str)
        if enum_matches:
            # enum_values에서 문자열을 리스트로 변환
            # 각 값을 ' '로 감싸져 있는 부분을 제거하고 쉼표로 분리
            enum_values = enum_matches.group(1).strip().split(',')
            # 각 enum 값에서 따옴표를 제거
            type_detail['enum_values'] = [value.strip().strip("'\"") for value in enum_values]

    return type_detail


def generate_data(fake, type_detail):
    data_type = type_detail['type']
    size = type_detail.get('size')
    decimal_place = type_detail.get('decimal_place')

    if data_type in ["INTEGER", "SMALLINT", "MEDIUMINT", "TINYINT"]:
        return random.randint(0, 10000) if data_type != "TINYINT" else random.randint(0, 255)

    elif data_type in ["CHAR", "VARCHAR", "TEXT"]:
        if data_type == "CHAR" and size:  # char
            return fake.lexify('?' * size)
        elif size:  # varchar
            return fake.text(max_nb_chars=size)
        else:  # text
            return fake.text()

    elif data_type == "DECIMAL":
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

    elif data_type == "ENUM":
        if 'enum_values' in type_detail:
            return random.choice(type_detail['enum_values'])
        else:
            return None

    else:
        return None


def run(engine, fake, n):
    table_list = table_modifier.get_all_tables_from_database(engine)
    for table in table_list:
        print(generator(fake, table, n))
