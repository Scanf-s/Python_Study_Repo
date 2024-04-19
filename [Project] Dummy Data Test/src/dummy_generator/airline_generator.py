import faker_airtravel
import sqlalchemy
from faker import Faker
from faker_airtravel import AirTravelProvider
from sqlalchemy import create_engine, MetaData, select, delete, text


def generate_airline_dummy_data(fake, n):
    check_duplicate_airline_id = set()
    check_duplicate_iata = set()
    dummy_data = []

    # airline_id, iata 집어넣을때마다 중복 체크 반드시 해줘야함
    for i in range(n):
        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_int
        airline_id = fake.random_int(min=0, max=32000)
        while airline_id in check_duplicate_airline_id:
            airline_id = fake.random_int(min=0, max=32000)
        check_duplicate_airline_id.add(airline_id)


        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.lexify
        # airtravel에서 제공하는 iata 생성 함수는 3자리라 못씀
        airline_iata = fake.lexify(text='??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        # iata가 UNIQUE인데 두자리라 중복될 가능성이 매우 높아서 set을 따로 두고 관리
        while airline_iata in check_duplicate_iata:
            airline_iata = fake.lexify(text='??', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        check_duplicate_iata.add(airline_iata)

        # https://pypi.org/project/faker_airtravel/
        airline_name = fake.airline()

        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_int
        base_airport = fake.random_int(min=0, max=32000)

        dummy_data.append((airline_id, airline_iata, airline_name, base_airport))

    return dummy_data