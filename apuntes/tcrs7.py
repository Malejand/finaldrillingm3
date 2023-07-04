# a = 5
# b = 10
# # iteraciones = 5
# cuenta = 0
# # while cuenta < a or cuenta < b and not cuenta >= iteraciones:
# #     print(f"Cuenta: { cuenta }, a: {a}, b: {b}")
# #     cuenta += 1
# while cuenta < a or cuenta < b:
#     print(a, b, cuenta)
#     cuenta += 1

acciones = {
    'AAPL': 187.31,
    'MSFT': 124.06,
    'FB': 183.50
}
for clave, valor in acciones.items():
    print(clave + " : " + str(valor))
