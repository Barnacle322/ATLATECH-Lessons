import math as mt
import random
from datetime import datetime, timedelta
from math import floor, pi
from math import sqrt as square_root

from numpy import round as np_round

print(square_root(25))
radius = 10
print(pi * radius**2)
mt.cos(10)

print(floor(3.5))
print(np_round(3.2))

now = datetime.now()
delta = timedelta(days=1)
tomorrow = now + delta

print(now.time())
print(now.date())

print(now.time().second)
print(now.time().minute)
print(now.time().hour)


jokes = [
    "Русалка села на шпагат",
    "Еврей нашел кошелек, а там не хватает",
    "Колобок повесился",
]

print(random.choice(jokes))
print(random.random())
print(random.randint(0, 100))

# Псевдо генератор случайных чисел(PRNG)
print(str(datetime.now().microsecond * 2388)[5])
