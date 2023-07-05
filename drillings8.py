lista = [[1, 2, 3], [0, 4, 5], [4, 0, 1], [6, 5, 4]]
diccionario = {}
claves = ["A", "B", "C", "D"]
contador = 0
for x in lista:
    diccionario[claves[contador]] = x
    contador += 1
    if x[0] == 0:
        continue
    for y in x:
        if y == 0:
            continue
        print(y)

print(diccionario)
# diccionario_lista = {}
# diccionario_lista["A"] = [1, 2, 3]
# diccionario_lista["B"] = [0, 4, 5]
# diccionario_lista["C"] = [4, 0, 1]
# diccionario_lista["D"] = [6, 5, 4]

# print(diccionario_lista)
