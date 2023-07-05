# FUNCIONES

# mi_nombre = input("ingrese su nombre")

def saludo(nombre, mensaje="Buenos dias"):
    print(nombre + " " + mensaje)
    return

# def  nombre_funcion(argumento1, argumento2 = valor default)


# saludo(mi_nombre)
saludo("Jose", "hola como estas?")


def suma(a, b, c):
    global resultado  # para que la variable pueda ser usada fuer ade la funcion
    resultado = a + b + c
    return resultado


# print(suma(10, 5))


# -> en esta variable -args- se almacenaran los argumentos ingresados como lista
def suma_varios(*args):
    resultado = 0
    for x in args:
        resultado += x
    return resultado


print(suma_varios(1, 3, 5, 8, 23, 8))  # -> args = [1,3,5,8,23]

# def apellido(**kwargs), todo lo ingresado lo considera como un diccionario


def nombre_completo(**persona):
    mensaje = "el apellido de " + \
        persona["nombre"] + " es " + persona["apellido"]
    return mensaje


print(nombre_completo(nombre="Jose", apellido="Hermosilla"))
