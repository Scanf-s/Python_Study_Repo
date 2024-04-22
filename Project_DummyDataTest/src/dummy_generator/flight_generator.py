import random
import string


def generate_flight_dummy_data(fake, n):
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
        departure_time = fake.date_time()
        arrival_time = fake.date_time_between(start_date=departure_time)

        airline_id = random.randint(1, 20001)
        airplane_id = random.randint(1, 20001)

        dummy_data.append((flightno, _from, _to, departure_time, arrival_time, airline_id, airplane_id))

    return dummy_data
