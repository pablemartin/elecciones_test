import random

from voting.tests.factories import VoterFactory

possible_dnis = range(100000, 10000000 + 1)
random_dnis = random.sample(possible_dnis, 100)

for dni in random_dnis:
    VoterFactory(dni=dni)


print('Padron creado')
