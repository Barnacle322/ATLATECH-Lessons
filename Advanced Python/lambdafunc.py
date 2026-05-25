names = ["Жантай", "Улугбек", "Адилет", "Арстан"]


names.sort(key=lambda name: len(name))
print(names)


numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x**2, numbers))


new_list = list(filter(lambda x: x % 2 == 0, numbers))
print(new_list)
