# # EJERCICIO 1
# mi_lista = [1, 2, 3, 4, 5]
# print(mi_lista[3])
# print(mi_lista[2:4])

# # EJERCICIO 2
# tup1 = (1, 2, 3, 4, 5, 6, 7)
# print(tup1[1:5])

# # EJERCICIO 3

# set1 = set(["Esto", "es", "un", "Ejercicio"])

# for x in set1:
#     print(x, end=" ")

# # EJERCICIO 4

# dict = {"Nombre": "Luis", "Apellido": "Gonzalez", "Edad": 21}
# print("Nombre :", dict["Nombre"])
# print("Edad: ", dict["Edad"])

# EJERCICIO 5

# la_lista = [10, 20, 14]
# la_tupla = (1, 2, 4, 6)
# el_set = {1000, 2000, 3000, 4000, 5000}

# print("Lista:", len(la_lista))
# print("Tupla:", len(la_tupla))
# print("Set:", len(el_set))

# EJERCICIO 6-calcular el numero de objetos

nro_frutas = {"Manzanas": 100, "Peras": 120, "Naranjas": 50}

print(len(nro_frutas))
# KEYS
X = nro_frutas.keys()
print("Cantidad de elementos:", len(X))
# O
elementos = nro_frutas.items()
print(len(elementos))
# VALUES
y = nro_frutas.values()
print("cantidad de elementos:", len(y))
