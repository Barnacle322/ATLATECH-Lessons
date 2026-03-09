my_list = [1, 2, 3, 4, 5, 6]
# print(my_list)
my_list.reverse()
# print(my_list)


my_list = [5, 1, 2, 6, 123]
my_list.sort()
# print(my_list)

my_tuple = (5, 3, 2, 1, 100)
my_sorted_tuple = tuple(sorted(my_tuple))
print(my_tuple)
print(my_sorted_tuple)

# Concatenation (Конкатенация) и интерполяция типов(casting)
my_int_string = int("123")
print(my_int_string + 10)

print(max(my_tuple))
print(min(my_tuple))
print(sum(my_tuple))
print(sum(my_tuple) / len(my_tuple))


# Dictionary methods (методы словарей)
my_dictionary: dict[str, int] = {"arstan": 22, "aliya": 21, "zhantai": 16}

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())
