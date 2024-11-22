"""
ciclos for python 
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
"""
System.out.println("1: 2");
    contador = 1;
    num = 3;
    while (contador < numPrimos){
esPrimo = true;
divisor=3;
while ((divisor<=Math.sqrt((num))) && esPrimo) {
if (num%divisor==0) {
esPrimo = false;
}
        divisor +=2;
      }
      if (esPrimo){
        contador +=1;
        System.out.println(contador + ": " + num);
      }
      num +=2;
    }
  }
}