# DICCIONARIOS

paises_y_capitales = {
    'Japon': 'Tokio',
    'Inglaterra': 'Londres',
    'Francia': 'Paris',
    'Alemania': 'Berlin'}

# ITERACIONES

# Para obtener un valor necesitamos ingresar su key
# print(paises_y_capitales["Japon"])

# keys = paises_y_capitales.keys()#muestra las keys del diccionario
# print(keys)

# for clave in keys:
#     print(f"{clave} - {paises_y_capitales[clave]}")

# for x in paises_y_capitales:  # entrega directamente las claves
#     print(x)

# values = paises_y_capitales.values()
# print(values)

# for capital in values:
#     print(capital)

# LA CUARTA FORMA DE ITERAR UN DICCIONARIO ES CON ITEMS
# print(paises_y_capitales.items())

for clave, valor in paises_y_capitales.items():
    print(f"el pais es {clave} y la capital es {valor}")
