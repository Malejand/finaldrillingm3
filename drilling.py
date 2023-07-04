palabra = ["p", "a", "r", "a", "l", "e",
           "l", "e", "p", "i", "p", "e", "d", "o"]
for val in palabra:
    if val == "a" or val == "e" or val == "i":
        continue
    print(f"{val} , {palabra.index(val)}")
