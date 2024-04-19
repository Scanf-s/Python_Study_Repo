from faker.generator import random
def generate_employee_dummy_data(fake, n):
    check_duplicate_username = set()
    dummy_data = []

    for i in range(n):
        # https://faker.readthedocs.io/en/stable/locales/en.html#faker.providers.person.en.Provider.first_name
        firstname = fake.first_name()
        lastname = fake.last_name()

        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.date_time.en_US.Provider.date_between
        birthdate = fake.date_between()

        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.passport.en_US.Provider.passport_gender
        sex = fake.passport_gender() if random.choice([True, False]) else None

        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.address.en_US.Provider.street_address
        street = fake.street_address()

        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.address.en_US.Provider.city
        city = fake.city()

        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.address.en_US.Provider.zipcode
        zipcode = int(fake.zipcode())
        while not 0 <= zipcode <= 32767:
            zipcode = int(fake.zipcode())

        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.address.en_US.Provider.country
        country = fake.country()

        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker.providers.internet.en_US.Provider.ascii_company_email
        emailaddress = fake.company_email() if random.choice([True, False]) else None

        # https://faker.readthedocs.io/en/stable/locales/en_US.html#faker-providers-phone-number
        telephoneno = fake.country_calling_code() + fake.basic_phone_number() if random.choice([True, False]) else None

        # https://faker.readthedocs.io/en/master/providers/faker.providers.python.html#faker.providers.python.Provider.pydecimal
        salary = fake.pydecimal(right_digits=2, left_digits=8, positive=True, min_value=2000, max_value=50000) if random.choice([True, False]) else None

        # enum ('Marketing','Buchhaltung','Management','Logistik','Flugfeld']
        # https://stackoverflow.com/questions/62724145/choosing-from-a-list-of-names-using-factory-boy-integrated-with-faker
        department_list = ['Marketing','Buchhaltung','Management','Logistik','Flugfeld']
        department = random.choice(department_list) if random.choice([True, False]) else None

        # https://stackoverflow.com/questions/73433408/how-to-create-a-random-login-with-faker-on-java
        username = fake.user_name() if random.choice([True, False]) else None
        while username in check_duplicate_username:
            username = fake.user_name() if random.choice([True, False]) else None
        check_duplicate_username.add(username)

        # https://faker.readthedocs.io/en/master/providers/faker.providers.misc.html#faker.providers.misc.Provider.password
        password = fake.password(special_chars=True, length=32) if username is not None else None

        dummy_data.append((firstname, lastname, birthdate, sex, street, city, zipcode, country, emailaddress, telephoneno, salary, department, username, password))

    return dummy_data
