import string


def generate_airplane_dummy_data(fake, n):
    # check_duplicate_airplane_id = set()
    dummy_data = []

    # airplane_id 집어넣을때마다 중복 체크 반드시 해줘야함
    for i in range(n):
        # https://faker.readthedocs.io/en/master/providers/baseprovider.html#faker.providers.BaseProvider.random_int
        # airplane_id = fake.random_int(min=0, max=100000)
        # while airplane_id in check_duplicate_airplane_id:
        #     airplane_id = fake.random_int(min=0, max=100000)
        # check_duplicate_airplane_id.add(airplane_id)
        # AUTO INCREMENT

        # mediumint unsigned : 0 ~ 16777215
        capacity = fake.random_int(min=2, max=10000000)

        # airplane_typedml type_id 참고
        type_id = fake.random_int(min=1, max=20001)

        # airline의 airline_id, small int임
        # airplane의 airline은 중복될 수 있으니까 airline primary key 상관 X
        airline_id = fake.random_int(min=1, max=32767)

        dummy_data.append((capacity, type_id, airline_id))

    return dummy_data
