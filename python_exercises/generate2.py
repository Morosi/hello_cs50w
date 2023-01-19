from random import choice
from random import randint
from time import sleep
while (4 < 5):
    coin = choice(['heads', 'tails'])
    print(coin)
    sleep(1)
    number = randint(20, 30)
    print(number)
    sleep(1)