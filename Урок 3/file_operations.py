scores = {
    "adilet": 60,
    "zhantai": 20,
    "ulugbek": 100,
    "aliya": 0,
}

# with open("./Урок 3/students.txt", "w") as file:
#     for name, score in scores.items():
#         file.write(f"{name} получил {score}\n")


with open("./Урок 3/students.txt", "r") as file:
    for line in file:
        int(line)
        print(line, end="")
