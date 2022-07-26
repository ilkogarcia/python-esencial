# Instrucción return para utilizar el resultado en el proceso
print()
def perimetro_cuadrado(lado):
    perimetro = lado * 4
    #return perimetro Cuando la función no devuelve un valor entonces se considera "None"

def area_cuadrado (lado):
    area = lado * lado
    return area

perimetro = perimetro_cuadrado(lado=5)
area = area_cuadrado(lado=5)

print(f"Área: {area}, Perímetro: {perimetro}")

# En una función se pueden devolver varios resultados al mismo tiempo
print()
def calcular_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return area, perimetro

area, perimetro = calcular_cuadrado(lado=5)

#print(f"Área: {area}, Perímetro: {perimetro}")

resultado = calcular_cuadrado(lado=5)
print(resultado)
