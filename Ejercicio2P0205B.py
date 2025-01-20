def factorialrecursivo(numero):
    """Función que calcula el factorial de un número entero.
    Parámetros:
            - n: Un número entero positivo.
    Salida:
            - El factorial del numero entero ingresado mediante mediante una función recursiva.
    """
    
    if numero == 0:
        return 1
    else:
        return numero*factorialrecursivo(numero-1)

factor = int(input("Por favor ingresa un numero entero para conocer su factorial:"))
resultadof = factorialrecursivo(factor)
print("El factorial de:", factor, "es:", resultadof)