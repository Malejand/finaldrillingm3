lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
for x in lista:
    if x[0] == 0:
        continue
    for y in x:
        if y == 0:
            continue
        print(y)
