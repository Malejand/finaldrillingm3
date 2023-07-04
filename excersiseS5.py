# EVALUANDO CON ELIF
# n = 0
# if n >= 0:
#     print(f"{n} es un numero mayor o igual a 0")
# else:
#     print(f"{n} es menor que 0")
# if n > 0:
#     print(f"{n} es un numero positivo")
# elif n == 0:
#     print(f"{n} es igual a cero")
# else:
#     print(f"{n} es un numeor negativo")

# ITERANDO UNA LISTA

# numeros = [6, 5, 3, 8, 4, 2, 5, 4, 11]
# suma = 0
# for elem in numeros:
#     suma = suma + elem
# print(suma)

# USANDO FOR ELSE
# digitos = [0, 1, 5]
# for i in digitos:
#     print(i)
# else:
#     print("no quedan elementos en la lista")
# i = 1
# suma = 0

# CONOCIENDO WHILE
# while i <= 10:
#     suma = suma + i
#     i += 1

# print(f"La suma es {suma}")

# SENTENCIA BREAK MUCHO MUY IMPORTANTEEEEEE
for val in "murcielago":
    if val == "c":
        break
    print(val)

print("Fin")

# SENTENCIA CONTINUE
for val in "cadena":
    if val == "a":
        continue
    print(val)
print("Fin")
