def pos(num):
    if num >= 0:
        return "El numero ingresado es Positivo"
    else:
        return "El numero ingresado es Negativo"
    
def factorial(num2):
    if num2==0 or num2==1:
        resultado=1
    elif num2>1:
        resultado=num2*factorial(num2-1)
    return resultado

def validarNumero(num3):
    try:
        int(num3)
        return "Si es un numero"
    except ValueError:
        return "No es un numero"

    
        