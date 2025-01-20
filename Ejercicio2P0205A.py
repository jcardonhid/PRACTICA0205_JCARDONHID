def factorial(n):
    """Función que calcula el factorial de un número entero.
    Parámetros:
       - n: Un número entero positivo.
    Salida:
       - El factorial del numero entero ingresado mediante bucles interactivos
    """
    
    f = 1
    for i in range(n):
        f = f * (i+1)
    return f

factor = int(input("Por favor ingresa un numero entero para conocer su factorial:"))
resultado = factorial(factor)
print("El factorial de:", factor, "es:", resultado)