def generate_airport_geo_dummy_data(fake, n):
    check_duplicate_airport_id = set()
    dummy_data = []

    for i in range(n):
        # smallint, primary key
        airport_id = fake.random_int(1, 32767)
        while airport_id in check_duplicate_airport_id:
            airport_id = fake.random_int(1, 32767)
        check_duplicate_airport_id.add(airport_id)

        # https://pypi.org/project/faker_airtravel/
        name = fake.airport_name()

        # https://faker.readthedocs.io/en/stable/providers/faker.providers.address.html
        city = fake.city()

        # https://faker.readthedocs.io/en/stable/providers/faker.providers.address.html#faker.providers.address.Provider.country
        country = fake.country()

        # https://faker.readthedocs.io/en/master/providers/faker.providers.geo.html
        latitude = fake.latitude()

        # https://faker.readthedocs.io/en/master/providers/faker.providers.geo.html#faker.providers.geo.Provider.longitude
        longitude = fake.longitude()

        dummy_data.append((airport_id, name, city, country, latitude, longitude))

    return dummy_data
