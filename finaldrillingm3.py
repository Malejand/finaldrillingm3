lalista = ["Harry Houdini", "David Blaine", "Teller",
           "Newton", "Hawking", "Einstein", "Messi", "Pele", "Juanes"]


def hacer_grandioso(arg):
    contador = 0
    for x in arg:
        arg[contador] = f"El gran {x}"
        contador += 1
    print(arg)


def imprimir_nombres(arg):
    print(arg)


imprimir_nombres(lalista)
hacer_grandioso(lalista[:3])
imprimir_nombres(lalista[3:])
