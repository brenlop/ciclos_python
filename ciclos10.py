"""
ciclos for python
 Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
"""
 base=float(input("Base:"))
 exp=int(input("Exponente:"))
 potencia=1
 for cont in range(1,exp+1):
     potencia=potencia*base
 print("Potencia=%f"%potencia)

