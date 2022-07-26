'''
Vamos a practicar con las estructuras de datos.
Las estructuras de datos son las formas que tiene
el lenguaje para organizar los datos, y nos permiten
realizan operaciones de manipulación, extracción,
búsqueda e inserción de manera eficiente.

Alguas estructuras de datos en Python son mutables,
lo que significa que sus elementos pueden ser modificados
despues de su creación.
'''


# ******
# Diccionarios, se representan entre llaves {llave: valor}
# Son estructuras no ordenadas, mutables y que no permiten duplicados
# contienen pares de llave y valor separados por dos punto y cada par de elemento por una coma

usuario = {
    "nombre": "Ilko",
    "apellido": "García",
    "edad": 47
}
print(usuario)
print(usuario["nombre"])

usuario["anio_nacimiento"] = 1994 # En un diccionario es posible agregar nuevos pares de llave:valor
print(usuario)

usuario["anio_nacimiento"] = 1974 # Un diccionario no permite duplicados por lo que actualizará los valores
print(usuario)

usuario["padres"] = ["Luis García", "Esperanza Pérez"] # Los diccionarios pueden contener listas
print(usuario)

print(usuario.items()) # Nos devolverá una lista con todas las tuplas del diccionario
print(usuario.keys()) # Nos devolverá una lista con las llaves dentro del diccionario
print(usuario.values()) # Nos devolverá una lista con los valores dentro del diccionario

usuario.clear() # Con esto haremos que el diccionario quede vacio
print(usuario)
