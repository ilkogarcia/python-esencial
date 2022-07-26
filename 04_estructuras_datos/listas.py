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
# Listas, se representan entre corchetes [elem_1, elem_2,..., elem_n]
# Son estructuras ordenadas, mutables y permiten duplicados

from turtle import update


lenguajes = ["python", "java", "golang"] # Declaración de una lista
print(lenguajes)

longitud_lista = len(lenguajes) # La función len nos dará la longitud de la lista
print(longitud_lista) 

print(lenguajes[0]) # Imprime la primera posición de una lista
print(lenguajes[-1]) # Imprime la última posición de una lista
print(lenguajes[-longitud_lista]) # Imprime la primara posición de una lista

print(lenguajes[0:2]) # Imprime lo elementos uno y dos de la lista

lista = [1, 2.0, True, "python", 1] #Las listas permiten duplicados y elementos de diferentes tipos
print(lista)

programacion = [lenguajes, "dedicación", "practica"] # Las listas pueden contener otras listas (listas anidadas)
print(programacion)
print(programacion[0][0])

lenguajes[0] = "dart" # Los elementos de una lista son mutables y por tanto pueden modificarse
print(lenguajes)

lenguajes.append("python") # Agregar elementos al final de una lista mediante append
print(lenguajes)

otros_lenguajes = ["C", "C++"]
lenguajes.extend(otros_lenguajes) # Extender una lista con otro lista usando extend
print(lenguajes)

lenguajes.append(otros_lenguajes) # Agregar una lista como un elemento de otra lista (listas anidadas)
print(lenguajes)
