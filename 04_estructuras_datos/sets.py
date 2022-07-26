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
# Sets, se representan entre llaves {elem_1, elem_2,..., elem_n}
# Son estructuras no ordenadas, mutables y contienen elementos únicos (no duplicados)

set1 = {1, 2, 3}
print(set1)

# set1[0] Esto debería dar un error

set2 = {1, 1, 1, 2, 3}
print(set2)

set3 = {1, 2.0, "texto"}
print(set3)

set1.add(4) # En un set se puede agregar elementos nuevos
print(set1)
print(len(set1))

set1.update([4, 5, 6]) # Un set puede actualizarse con ultiples elementos nuevos
print(set1)
print(len(set1))

set1.discard(2) # Es sencillo eliminar del set un elemento de esta manera
print(set1)
print(len(set1))

set1.remove(3) # También se puede usar esta otra manera para eliminar un elemento
print(set1)
print(len(set1))

set1.clear() # Con este método podemos vaciar el set
print(set1)

