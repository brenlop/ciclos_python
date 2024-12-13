'''
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''

cantidad = int(input("Introduce la cantidad de números primos y mostrar: "))


numero = 2  
mostrador = 0  


while mostrador < cantidad:
    es_primo = True
    
    
    for i in range(2, int(numero ** 0.5) + 1):
        
        if numero % i == 0:
            es_primo = False
            break
    
    
    if es_primo:
        print(numero)
        mostrador += 1
    
    
    numero += 1
