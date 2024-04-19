import random
import string


def generate_flight_log_dummy_data(fake, n):
    dummy_data = []
    for i in range(n):
        log_date = fake.date_time_this_decade()
        user = fake.user_name()

        flight_id = random.randint(100000, 500000)

        flightno_old = fake.bothify(text='???-####', letters=string.ascii_uppercase)
        flightno_new = fake.bothify(text='???-####', letters=string.ascii_uppercase)

        from_old = random.randint(1, 100)
        to_old = random.randint(1, 100)
        from_new = random.randint(1, 100)
        to_new = random.randint(1, 100)

        # https://faker.readthedocs.io/en/master/locales/ar_AA.html#faker.providers.date_time.ar_AA.Provider.date_time_this_year
        departure_old = fake.date_time_this_year(before_now=True, after_now=False)
        arrival_old = fake.date_time_this_year(before_now=True, after_now=False)
        departure_new = fake.date_time_this_year(before_now=False, after_now=True)
        arrival_new = fake.date_time_this_year(before_now=False, after_now=True)

        airplane_id_old = random.randint(1, 20001)
        airplane_id_new = random.randint(1, 20001)
        airline_id_old = random.randint(1, 20001)
        airline_id_new = random.randint(1, 20001)

        comment = fake.text(max_nb_chars=200) if random.choice([True, False]) else None

        dummy_data.append(
            (log_date,
             user,
             flight_id,
             flightno_old,
             flightno_new,
             from_old,
             to_old,
             from_new,
             to_new,
             departure_old,
             arrival_old,
             departure_new,
             arrival_new,
             airplane_id_old,
             airplane_id_new,
             airline_id_old,
             airline_id_new,
             comment))

    return dummy_data
