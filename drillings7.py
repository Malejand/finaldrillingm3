lista = [[1, 2, 3],
         [0, 4, 5],
         [4, 0, 1],
         [6, 5, 4],
         ]
nueva = []
for x in lista:
    if lista[0][0] == 0 or lista[1][0] == 0 or lista[2][0] == 0 or lista[3][0] == 0:
        continue
    print(lista)
