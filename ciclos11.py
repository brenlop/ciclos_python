"""
ciclos for python 
Escribe un programa que diga si un número introducido por teclado es o no primo. 
Un número primo es aquel que sólo es divisible entre él mismo y la unidad. 
Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es 
divisible por algún otro número.
"""
console.write("ingrese un número: ")
num = cint(console.readline())

esprimo = true

if num <= 1 then
    esprimo = false
else
    for i = 2 to math.sqrt(num)
        if num mod i = 0 then
            esprimo = false
            exit for
        end if
    next
end if

if esprimo then
    console.writeline(num & " es un número primo.")
else
    console.writeline(num & " no es un número primo.")
end if

console.readkey()