user_input = input("Введите ваш индекс: ")

try:
    my_tuple = [1, 2, 3, 4, 5]
    print(my_tuple[int(user_input)])
except Exception:
    print("And error happened")

print("asdf")
