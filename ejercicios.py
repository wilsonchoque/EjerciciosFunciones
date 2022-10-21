import misfunciones as mf

#1.	Crear una función que te permita evaluar si un número ingresado es positivo o negativo (agregarla a su biblioteca de funciones).
numero = float(input("(Positivo o Negativo)Ingrese un numero: "))
print(mf.pos(numero))

#2. Crear una función para hallar la factorial de un número.
numero = float(input("(Hallar Factorial) Ingrese un numero: "))
print(mf.factorial(numero))

#3. Crear una función que valide si lo ingresado por teclado es un número.
numero = input("(Validar si es Numero) Escriba un numero: ")
print(mf.validarNumero(numero))