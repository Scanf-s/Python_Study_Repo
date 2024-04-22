import string


def generate_airplane_dummy_data(fake, n):
    dummy_data = []

    for i in range(n):
        # mediumint unsigned : 0 ~ 16777215
        capacity = fake.random_int(min=2, max=10000000)

        # airplane_type의 type_id 참고
        type_id = fake.random_int(min=1, max=20001)
        airline_id = fake.random_int(min=1, max=32767)

        dummy_data.append((capacity, type_id, airline_id))

    return dummy_data
