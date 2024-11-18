"""

ciclo for en python 

Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.
 
# Función para imprimir la tabla de multiplicar de un número dado
def imprimir_tabla(numero):
    for i in range(1, 11):
        print(f'{numero} x {i} = {numero * i}')
    print('')  # Línea en blanco para separar las tablas

# Imprimir las tablas de multiplicar del 1 al 5
for numero in range(1, 6):
    imprimir_tabla(numero)
