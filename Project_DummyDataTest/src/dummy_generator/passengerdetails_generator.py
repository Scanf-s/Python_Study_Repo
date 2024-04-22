import random


def generate_passengerdetails_dummy_data(fake, n):
    check_duplicate_passenger_id = set()
    dummy_data = []
    for i in range(n):
        passenger_id = random.randint(1, 20001)
        while passenger_id in check_duplicate_passenger_id:
            passenger_id = random.randint(1, 20001)
        check_duplicate_passenger_id.add(passenger_id)

        birthdate = fake.date()
        sex = fake.passport_gender() if random.choice([True, False]) else None
        street = fake.street_address()
        city = fake.city()
        zipcode = int(fake.zipcode())
        while not 0 <= zipcode <= 32767:
            zipcode = int(fake.zipcode())
        country = fake.country()
        emailaddress = fake.company_email() if random.choice([True, False]) else None
        telephoneno = fake.country_calling_code() + fake.basic_phone_number() if random.choice([True, False]) else None

        dummy_data.append((passenger_id, birthdate, sex, street, city, zipcode, country, emailaddress, telephoneno))

    return dummy_data
