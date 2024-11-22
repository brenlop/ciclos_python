"""
ciclos for python 
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
"""
roceso PagoEn20Meses
    total <- 0;
    Para i<-1 Hasta 20 Con Paso 1 Hacer
        Escribir "PROCESO ", i;
        Si i = 1 Entonces
            pago <- 10;
        SiNo
            pago <- pago*2;
        FinSi
        total <- total+pago;
        Escribir "Valor de pago: ", pago;
        Escribir "";
    FinPara
    Escribir "Valor de total: ", total;