def converdec(numero):
    """Función que convierte un número binario en decimal.
    Parámetros:
        numero: Es una cadena formada por unos y ceros.
    Devuelve:
        El equivalente en decimales de: numero.
    """
    numero = list(numero)
    numero.reverse()
    converdec = 0
    for i in range(len(numero)):
        converdec += int(numero[i]) * 2 ** i
    return converdec

def converbin(numero):
    """Función que convierte un número decimal en binario.
    Parámetros:
        numero: Es un número entero.
    Devuelve:
        El equivalente binario de: numero.
    """
    converbin = []
    while numero > 0:
        converbin.append(str(numero % 2))
        numero //= 2
    converbin.reverse()
    return ''.join(converbin)

selec = input("Ingreas B si quieres convertir a binario o D si quieres convertir a decimal:")

if selec == "B":
    deci = int(input("Ingresa el número decimal que quieres convertir a binario:"))
    print("El equivalente binario de", deci, "es:", converbin(deci))
elif selec == "D":
    bina = str(input("Ingresa el número binario que quieres convertir a decimal:"))
    print("El equivalente decimal de", bina, "es:", converdec(bina))