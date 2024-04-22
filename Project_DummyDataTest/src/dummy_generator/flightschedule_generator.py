import random
import string


def generate_flightschedule_dummy_data(fake, n):
    check_duplicate_flightno = set()
    dummy_data = []
    for i in range(n):
        flightno = fake.bothify(text="???-####", letters=string.ascii_uppercase)
        while flightno in check_duplicate_flightno:
            flightno = fake.bothify(text="???-####", letters=string.ascii_uppercase)
        check_duplicate_flightno.add(flightno)

        _from = random.randint(1, 20001)
        _to = random.randint(1, 20001)

        # https://faker.readthedocs.io/en/master/providers/faker.providers.date_time.html#faker.providers.date_time.Provider.date_time
        departure_time = fake.time()
        # 날짜가 아니니까 arrival_time은 departure_time보다 작아도 상관 X
        arrival_time = fake.time()

        airline_id = random.randint(1, 20001)

        monday = 1 if random.choice([True, False]) else 0
        tuesday = 1 if random.choice([True, False]) else 0
        wednesday = 1 if random.choice([True, False]) else 0
        thursday = 1 if random.choice([True, False]) else 0
        friday = 1 if random.choice([True, False]) else 0
        saturday = 1 if random.choice([True, False]) else 0
        sunday = 1 if random.choice([True, False]) else 0
        dummy_data.append((
            flightno, _from, _to, departure_time, arrival_time, airline_id, monday, tuesday,
            wednesday, thursday, friday, saturday, sunday))

    return dummy_data
