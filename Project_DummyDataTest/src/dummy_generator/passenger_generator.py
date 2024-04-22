def generate_passenger_dummy_data(fake, n):
    check_duplicate_passportno = set()
    dummy_data = []
    for i in range(n):
        # https://faker.readthedocs.io/en/master/providers/faker.providers.passport.html
        passportno = fake.passport_number()
        while passportno in check_duplicate_passportno:
            passportno = fake.passport_number()
        check_duplicate_passportno.add(passportno)

        first_name = fake.first_name()
        last_name = fake.last_name()

        dummy_data.append((passportno, first_name, last_name))
    return dummy_data
