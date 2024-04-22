import random


def generate_weatherdata_dummy_data(fake, n):
    check_duplicate_log_date = set()
    check_duplicate_time = set()
    check_duplicate_station = set()
    dummy_data = []
    for i in range(n):
        log_date = fake.date()
        while log_date in check_duplicate_log_date:
            log_date = fake.date()
        check_duplicate_log_date.add(log_date)

        _time = fake.time()
        while _time in check_duplicate_time:
            _time = fake.time()
        check_duplicate_time.add(_time)

        station = random.randint(1, 20001)
        while station in check_duplicate_station:
            station = random.randint(1, 20001)
        check_duplicate_station.add(station)

        temperature = float(fake.decimal(left_digits=2, right_digits=1, positive=True))

        humidity = float(fake.decimal(left_digits=3, right_digits=1, positive=True))

        airpressure = float(fake.decimal(left_digits=8, right_digits=2, positive=True))

        wind = float(fake.decimal(left_digits=3, right_digits=2, positive=True))

        weather_enums = ['Nebel-Schneefall', 'Schneefall', 'Regen', 'Regen-Schneefall', 'Nebel-Regen',
                         'Nebel-Regen-Gewitter', 'Gewitter', 'Nebel', 'Regen-Gewitter']
        weather = random.choice(weather_enums) if random.choice([True, False]) else None

        winddirection = random.randint(0, 360)

        dummy_data.append((log_date, _time, station, temperature, humidity, airpressure, wind, weather, winddirection))

    return dummy_data