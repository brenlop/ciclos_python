"""
ciclos for en python 

un programa que permita adivinar un número. La aplicación genera un 
número aleatorio del 1 al 100. A continuación va pidiendo números y va 
respondiendo si el número a adivinar es mayor o menor que el introducido,
a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). 
El programa termina cuando se acierta el número (además te dice en cuantos 
intentos lo has acertado), si se llega al limite de intentos te muestra el 
número que había generado.
Para genear un número entero aleatorio se utiliza la función randint
del paquete random

estructura:
Module Program
    Sub Main()
        Dim aleatorio As Integer
        Dim intentos As Integer = 10
        Dim numero As Integer

        ' Generar número aleatorio entre 1 y 100
        Randomize()
        aleatorio = CInt(Rnd() * 100) + 1

        Console.WriteLine("Adivine el número entre 1 y 100")

        Do While intentos > 0
            Console.Write("Ingrese un número: ")
            numero = CInt(Console.ReadLine())

            If numero < aleatorio Then
                Console.WriteLine("El número a adivinar es mayor")
            ElseIf numero > aleatorio Then
                Console.WriteLine("El número a adivinar es menor")
            Else
                Console.WriteLine($"Felicitaciones! Adivinaste el número en {10 - intentos + 1} intentos")
                Return
            End If

            intentos -= 1
            Console.WriteLine($"Intentos restantes: {intentos}")