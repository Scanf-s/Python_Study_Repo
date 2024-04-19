import string
import random

def generate_booking_dummy_data(fake, n):
    check_duplicate_flight_id = set()
    check_duplicate_seat = set()
    dummy_data = []

    for i in range(n):
        # int, auto_incr, primary_key
        # booking_id

        # int, unique
        # 항공기 번호가 아니라, 예약 번호인 것 같다.
        flight_id = fake.random_int(100000, 500000)
        while flight_id in check_duplicate_flight_id:
            flight_id = fake.random_int(100000, 500000)
        check_duplicate_flight_id.add(flight_id)

        # char(4), unique
        seat = fake.bothify('??##', letters=string.ascii_uppercase) if random.choice([True, False]) else None
        while seat in check_duplicate_seat:
            seat = fake.bothify('??##', letters=string.ascii_uppercase) if random.choice([True, False]) else None
        check_duplicate_seat.add(seat)

        # int
        passenger_id = fake.random_int(min=10000, max=30001)

        # decimal(10, 2)
        # https://faker.readthedocs.io/en/master/providers/faker.providers.python.html#faker.providers.python.Provider.pydecimal
        price = fake.pydecimal(right_digits=2, left_digits=10, positive=True, min_value=1, max_value=10000)

        dummy_data.append((flight_id, seat, passenger_id, float(price)))

    return dummy_data
