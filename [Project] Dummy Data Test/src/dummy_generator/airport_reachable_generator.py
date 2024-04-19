import random


def generate_airport_reachable_dummy_data(fake, n):
    check_duplicate_airport_id = set()
    dummy_data = []

    for i in range(n):
        # smallint, primary key
        airport_id = fake.random_int(1, 32767)
        while airport_id in check_duplicate_airport_id:
            airport_id = fake.random_int(1, 32767)
        check_duplicate_airport_id.add(airport_id)

        # int
        hops = fake.random_int(1, 100) if random.choice([True, False]) else None

        dummy_data.append((airport_id, hops))

    return dummy_data