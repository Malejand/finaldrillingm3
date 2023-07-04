# LISTAS
pokemones = [
    "bulbasaur",
    "ivysaur",
    "venusaur",
    "charmander",
    "charmeleon",
    "charizard",
    "squirtle",
    "wartortle",
    "blastoise",
    "caterpie"
]
# APPEND PERMITE AGREGAR ELEMENTOS A UNA LISTA
pokemones.append("Metapod")
# print(pokemones)

otros_pokemones = ["Goldeen", "Seaking", "staryu", "starmie"]

# PARA AGREGAR VARIOS ELEMENTOS ATRAVES DE UNA LISTA
# for pokemon in otros_pokemones:
#     pokemones.append(pokemon)

# AGREGAR UNA LISTA DE POKEMONES A LA LISTA ORIGINAL
pokemones.extend(otros_pokemones)
# print(pokemones)


# INSERTAR ELEMENTOS CON METODO INSERT

pokemones.insert(1, "Magmar")
# print(pokemones)

"""METODOS PARA REMOVER ELEMENTOS"""

# REMUEVE UN ELEMENTO ESPECIFICO
# pokemones.remove("venusaur")
# print(pokemones)

# SI NO SE ENTREGA UN INDICE, pop() REMUEVE EL ULTIMO ELEMENTO DE LISTA
pokemones.pop()
pokemones.pop(1)
# print(pokemones)

# METODOS PARA SET----------------------------------------------------------------------------

mi_set = set()
# AGREGAR UN ELEMENTO
mi_set.add(1)
mi_set.add(2)
print(mi_set)

# PARA AGREGAR MAS DE UN ELEMENTO
mi_set.update(otros_pokemones)
print(mi_set)

# PARA ELIMINAR ELEMENTOS DEL SET

# mi_set.remove("starmie")
# print(mi_set)

mi_set.discard("starmie")
print(mi_set)

# POP ELIMINA EL PRIMER ELEMENTO
mi_set.pop()
print(mi_set)

# PARA ELIMINAR TODOS LOS ELEMENTOS DEL SET
mi_set.clear()
print(mi_set)
