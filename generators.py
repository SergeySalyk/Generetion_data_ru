from faker import Faker
from random import randrange, randint
import random
from datetime import date, timedelta
import uuid

fake = Faker(['ru_RU'])
Faker.seed(randint(2, 1000))


def generate_okpo_for_juridical():
    while True:
        number_random = randrange(4444444, 5555555)
        number = str(number_random)
        if number and len(number) == 7:
            break
    s1 = sum((pos + 1) * int(num) for pos, num in enumerate(number))
    s2 = 0
    for pos, num in enumerate(number):
        s2 += (pos + 1) * int(num)
    checkdigit = s1 % 11
    okpo = str(number) + str(checkdigit)
    return okpo


def generate_okpo_for_branch():
    while True:
        number_random = randrange(111111111, 999999999)
        number = str(number_random)
        if number and len(number) == 9:
            s1 = sum((pos + 1) * int(num) for pos, num in enumerate(number))
            s2 = 0
            for pos, num in enumerate(number):
                s2 += (pos + 1) * int(num)
            checkdigit = s1 % 11
            okpo_branch = str(number) + str(checkdigit) + '312333'
            return okpo_branch


def generate_passport_series():
    digits = str(randint(1000, 9999))
    return f"{digits}"


def generate_number():
    digits = str(randint(100000, 999999))
    return f"{digits}"


def generate_sor_number():
    roman_numeral = random.choice(['II', 'IV', 'VI', 'IX', 'XI'])
    russian_letter = ''.join([chr(random.randint(1040, 1071)) for i in range(2)])
    return f"{roman_numeral}-{russian_letter}"


def generate_name_city():
    return fake.city_name()


def generate_full_name_org():
    return fake.city_name()


def generate_kpp():
    return fake.kpp()


def generate_phone():
    return fake.phone_number()


def generate_pasport_number():
    return fake.plate_number_extra()


def generate_businesses_ogrn():
    return fake.businesses_ogrn()


def generate_businesses_inn():
    return fake.businesses_inn()


def generate_businesses_bic():
    return fake.bic()


def generate_businesses_inn_str():
    businesses_inn = fake.businesses_inn()
    return str(businesses_inn)


def generate_date_child():
    current_date = date.today()
    min_age = 1
    max_age = 8
    min_birthdate = current_date - timedelta(days=max_age*365)
    max_birthdate = current_date - timedelta(days=min_age*365)
    birthdate = current_date - timedelta(days=randint(min_age*365, max_age*365))
    return birthdate.strftime("%d.%m.%Y")


def generate_date_child_adult():
    current_date = date.today()
    min_age = 14
    max_age = 18
    min_birthdate = current_date - timedelta(days=max_age*365)
    max_birthdate = current_date - timedelta(days=min_age*365)
    birthdate = current_date - timedelta(days=randint(min_age*365, max_age*365))
    return birthdate.strftime("%d.%m.%Y")


def generate_date_adult():
    current_date = date.today()
    min_age = 18
    max_age = 40
    min_birthdate = current_date - timedelta(days=max_age*365)
    max_birthdate = current_date - timedelta(days=min_age*365)
    birthdate = current_date - timedelta(days=randint(min_age*365, max_age*365))
    return birthdate.strftime("%d.%m.%Y")


def generate_guid():
    return str(uuid.uuid4())