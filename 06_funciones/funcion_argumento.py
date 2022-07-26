''''
Las funciones son bloques de código independientes
que contienen instrucciones relacionadas entre si
que se encargan de cumplir con una tarea.

VENTAJAS:
- Organizar el código en partes pequeñas.
- Permite la organización y usabilidad del código.
- Evita la repetición de instrucciones y facilita su reutilización.

DEFINICIÓN:
def ejemplo_funcion(parametros, *args, **kwargs):
    Docstring
    <instrucciones>
    return variables

LLAMADA:
variable = ejemplo_funcion(parametro=1)

PARÁMETRO: Variables que ingresan a la función (Nombre)
ARGUMENTO: Variables que ingresan a la función (Valor)
*args: Permite pasar un número variable de argumentos a una función
**Kwargs: Similar a args pero los parámetros se pasan en forma de diccionarios
Retorno: Resultados

'''

APELLIDO = "García" 


# User defined functions
def mifuncion():
    print("Mi primera funcion")
    nombre = "Ilko"
    print(nombre, APELLIDO)
mifuncion()

# print(nombre) # Dará error porque la variable es local en el ámbito de la función
print(APELLIDO) # No dará error porque es una variable global

print()
def perimetro_cuadrado(lado, unidades):
    perimetro = lado * 4
    print(f"El perimetro es {perimetro} {unidades}")

perimetro_cuadrado(25, "metros")

perimetro_cuadrado(lado=10, unidades="cm")
