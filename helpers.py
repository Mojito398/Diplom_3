from faker import Faker

fake = Faker()
fakeRU = Faker(locale='ru_RU')


def create_random_email():
    email = fake.free_email()
    return email


def create_random_password():
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return password


def create_random_name():
    username = fakeRU.first_name()
    return username