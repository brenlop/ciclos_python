"""
ciclo for en python

 un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)

estructura:
#include <stdio.h>

int main() {
    int num;
    long factorial = 1;

    printf("Ingrese un número: ");
    scanf("%d", &num);

    if (num < 0)
     { printf("Error: El número debe ser positivo.\n");
     return 1;}
    for (int i = 1; i <= num; i++) 
    {factorial *= i;}

