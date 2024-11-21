"""
ciclos for python 
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
"""
estructura:
Console.WriteLine("Ingrese la cantidad de dinero que depositará cada mes:")

For i As Integer = 1 To meses
    Console.Write("Mes " & i & ": ")
    ahorradoMensual = CDbl(Console.ReadLine($1000))
    ahorradoAnual += ahorradoMensual
    Console.WriteLine("Ahorrado hasta el mes " & i & ": " & ahorradoAnual & vbCrLf)

