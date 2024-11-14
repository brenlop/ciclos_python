"""
ciclo for en python

permite realizar una serie de instrucciones 
una cantidad determinada de veces

estructura:
for i in [1...n]:
     instrucciones

range (fin)
    range (3)    [0,1,2]
range(inicio,fin)
    range(4,7)   [4,5,6] 
range(inicio,fin,pasos)
range(2,9,2)     [2,4,6,8]
"""

# ejercicio:imprimir los numeros del 1 al 10
for i in range (10):
    print(f"num: {1 +1} " )


# ejemplo:imprimir los numeros del 10 al 20 
for i in range (10,21):
    print(f"num: {i}")
# imprinir pares del 0 al 20 
for i in range (0,21,2):
    print(f"{i}")

