import string


def generate_airplane_type_dummy_data(fake, n):
    # check_duplicate_type_id = set()
    dummy_data = []

    # type_id 집어넣을때마다 중복 체크 반드시 해줘야함
    for i in range(n):
        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_int
        # type_id = fake.random_int(min=10000, max=50000)
        # while type_id in check_duplicate_type_id:
        #     type_id = fake.random_int(min=10000, max=50000)
        # check_duplicate_type_id.add(type_id)
        # INT, AUTO INCREMENT라 주석처리

        # https://www.icao.int/publications/DOC8643/Pages/Search.aspx
        # 해당 페이지의 Type Designator를 identifier로 사용했음
        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.bothify
        # https://www.geeksforgeeks.org/python-string-ascii_uppercase/
        identifier = fake.bothify('??##', letters=string.ascii_uppercase)

        # https://faker.readthedocs.io/en/master/providers/faker.providers.lorem.html#faker.providers.lorem.Provider.text
        description = fake.text(max_nb_chars=100)

        dummy_data.append((identifier, description))

    return dummy_data
