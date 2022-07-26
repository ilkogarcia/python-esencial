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
# Tuplas, se representan entre paréntesis (elem_1, elem_2,..., elem_n)
# Son estructuras ordenadas, inmutables y permiten duplicados

paises_europa = ("Portugal", "España", "Francia", "Alemania")
print(paises_europa)
paises_europa[0]
paises_europa[-1]

paises_asia = "China", "India", "Pakistan"
print(paises_asia)
paises_asia[0]
paises_asia[-1]

# paises_europa[-1] = "Marruecos" Daría error porque las tuplas no soportan la asignación de nuevas variables

paises_mundo = paises_europa + paises_asia # Varias tuplas se pueden concatenar
print(paises_mundo)
