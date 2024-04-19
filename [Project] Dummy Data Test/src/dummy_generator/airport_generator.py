import faker_airtravel
import sqlalchemy
from faker import Faker
from faker_airtravel import AirTravelProvider
from sqlalchemy import create_engine, MetaData, select, delete, text


def generate_airport_dummy_data(fake, n):
    check_duplicate_airport_id = set()
    check_duplicate_icao = set()

    dummy_data = []

    # airport id, icao 집어넣을때 마다 반드시 중복체크
    for i in range(n):
        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_int
        airport_id = fake.random_int(min=0, max=32000)
        while airport_id in check_duplicate_airport_id:
            airport_id = fake.random_int(min=0, max=32000)
        check_duplicate_airport_id.add(airport_id)

        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.lexify
        airport_iata = fake.airport_iata()

        # https://pypi.org/project/faker_airtravel/
        airport_icao = fake.airport_icao()
        while airport_icao in check_duplicate_icao:
            airport_icao = fake.airport_icao()
        check_duplicate_icao.add(airport_icao)

        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_int
        airport_name = fake.airport_name()

        dummy_data.append((airport_id, airport_iata, airport_icao, airport_name))

    return dummy_data