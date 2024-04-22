import string

def generate_airline_dummy_data(fake, n):
    check_duplicate_iata = set()
    dummy_data = []

    for i in range(n):
        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_int
        # airline_id = fake.random_int(min=0, max=32000)
        # while airline_id in check_duplicate_airline_id:
        #     airline_id = fake.random_int(min=0, max=32000)
        # check_duplicate_airline_id.add(airline_id)
        # AUTO INCREMENT라 굳이 넣을필요 없을것같다
        # 나중에, 다른테이블 attribute로 auto increment가 아닌 airline_id 넣을 때, small integer 범위 맞춰서 넣어주면 될듯

        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.lexify
        # airtravel에서 제공하는 iata 생성 함수는 3자리라 못씀
        airline_iata = fake.lexify(text='??', letters=string.ascii_uppercase)
        # iata가 UNIQUE인데 두자리라 중복될 가능성이 매우 높아서 set을 따로 두고 관리
        while airline_iata in check_duplicate_iata:
            airline_iata = fake.lexify(text='??', letters=string.ascii_uppercase)
        check_duplicate_iata.add(airline_iata)

        # https://pypi.org/project/faker_airtravel/
        airline_name = fake.airline()

        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_int
        base_airport = fake.random_int(min=0, max=32000)

        dummy_data.append((airline_iata, airline_name, base_airport))

    return dummy_data
