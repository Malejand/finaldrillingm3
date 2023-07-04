datos_personales = {
    "nombre": "antonio",
    "apellido": "lopez"
}

# AGREGAR DATOS A UN DICCIONARIO

datos_personales["edad"] = 30
datos_personales["peso"] = 80
datos_personales["altura"] = 2.0
print(datos_personales)
# print("nombre:", datos_personales["nombre"])
# print("edad:", datos_personales["edad"])

# ELIMINAR DATOS DE UN DICT

del datos_personales["peso"]
print(datos_personales)

# ELIMINAR TODOS LOS DATOS DEL DICT

datos_personales.clear()
print(datos_personales)
