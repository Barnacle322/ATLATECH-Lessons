import math
import os
import random
from datetime import datetime

print(math.sqrt(25))
print(math.pi)
print(round(10.6))
print(math.floor(10))


print(random.randint(1, 10))
print(random.choice(["Arstan", "Zhantai", "Ulugbek"]))

now = datetime.now()
print(now)
print(now.strftime("%d.%m.%y"))

print(os.getcwd())
print(os.listdir("."))
