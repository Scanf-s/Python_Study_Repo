import string


def generate_airplane_type_dummy_data(fake, n):
    dummy_data = []
    for i in range(n):
        # https://www.icao.int/publications/DOC8643/Pages/Search.aspx
        # 해당 페이지의 Type Designator를 identifier로 사용했음
        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.bothify
        # https://www.geeksforgeeks.org/python-string-ascii_uppercase/
        identifier = fake.bothify('??##', letters=string.ascii_uppercase)

        # https://faker.readthedocs.io/en/master/providers/faker.providers.lorem.html#faker.providers.lorem.Provider.text
        description = fake.text(max_nb_chars=100)

        dummy_data.append((identifier, description))

    return dummy_data
