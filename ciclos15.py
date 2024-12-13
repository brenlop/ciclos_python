"""
ciclo while

while exp_booleana:
    instrucciones
    acatualizacion de valores
"""

num = 1
while num < 10:
    print(f"Hello {num}")
    num = num + 5

    # Mas operadores matematicos
"""
n = n + 5 == n +=5
n = n - 5 == n -=5
n = n * 5 == n *=5
n = n / 5 == n /=5
"""

"""
Implementacion Do while (hacer, hasta) en python

while True:
   instruciones
   if exp_bool:
    breack
"""

while True:
    option = input("escribe salir: ")
    if option.upper == "salir":
        break
