"""

ciclos for en python

Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.
Para este problema se requiere de un acumulador y un contador
Contador: Variable que va, como su nombre lo indica, contando elementos (iteraciones),
por cada iteración el contador va incrementando en 1
"""
#include <iostream
using namespace std;

int main(int argc, char *argv[]) {
	int num;
	int suma,cont;
	float media;
	suma = 0;
	cont = 0;
	//Con el mientras si el primer número es 0 no va a entrar en el bucle
	cout << "Número (0 para salir):";
	cin >> num;
	while(num!=0) {
		suma = suma + num;
		cont = cont + 1;
		cout << "Número (0 para salir):";
		cin >> num;
	}
	//Si cont=0 no puedo realizar la división
	if(cont>0) {
		media = float(suma) / cont;
	}
	else
	{
		media =0;
	}
	cout << "Suma:" << suma << endl;
	cout << "Media:" << media;
	return 0;