import random

while True:
    i = int(input("Введите число: "))
    r = random.randint(0, 10)

    if i == r:
        print("correct")
    else:
        print("incorrect")