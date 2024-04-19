def generate_airport_dummy_data(fake, n):
    check_duplicate_icao = set()
    dummy_data = []
    for i in range(n):
        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.lexify
        airport_iata = fake.airport_iata()

        # https://pypi.org/project/faker_airtravel/
        airport_icao = fake.airport_icao()
        while airport_icao in check_duplicate_icao:
            airport_icao = fake.airport_icao()
        check_duplicate_icao.add(airport_icao)

        # https://pypi.org/project/faker_airtravel/
        airport_name = fake.airport_name()

        dummy_data.append((airport_iata, airport_icao, airport_name))

    return dummy_data