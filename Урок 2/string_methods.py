my_string = "          arstan89  useNov"
print(my_string)
parsed = (
    my_string.strip().replace("8", "").replace("9", "").title().split()
)  # -> ['arstan', 'usenov']
final = " ".join(parsed)
print(final)
