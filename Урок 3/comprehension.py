# Возведите все числа во вторую степень
my_list = [1, 2, 3, 4, 5]

squares = []
for i in my_list:
    if i % 2 == 0:
        squares.append(i**2)

print(squares)

# List comprehension (Генератор списков)
squares = [i**2 for i in my_list if i % 2 == 0]
print(squares)

# Set comprehension
names = ["adilet", "arstan", "ulugbek", "zhantai", "aliya"]
formatted_names = {name.capitalize() for name in names}
print(formatted_names)

# Dict comprehension
scores = {"adilet": 60, "zhantai": 20, "ulugbek": 100, "aliya": 0}
# scores.items() -> [('adilet', 60), ('zhantai', 20), ('ulugbek', 100), ('aliya', 0)]
# name, score = ("adilet", 60)
passing = {name: score for name, score in scores.items() if score >= 60}
print(passing)

# Tuple comprehension
elements = ("hydrogen", "helium", "alluminium", "oxygen")
short_elements = tuple(element for element in elements if len(element) < 7)
print(short_elements)