import random
from datetime import date

from faker import Faker

from voting.models import Voter


range_total = list(range(100))
padron_total = random.shuffle(range_total)
faker = Faker()

for i in range_total:
    name = faker.name().split(' ')
    dni = random.randrange(100000, 10000000)
    año = random.randrange(1940, 2005)
    mes = random.randrange(1, 12)
    dia = random.randrange(1, 30)
    Voter.objects.create(
        first_name=name[0], last_name=name[1], dni=dni, birth_date=date(año, mes, dia)
    )

print('Padron creado')
