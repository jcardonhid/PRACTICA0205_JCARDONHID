def contador1(texto):
    """Función que recibe un fragmento de texto en una cadena de caracteres y
        devuelve un diccionario con cada palabra que contiene y su frecuencia.
    Parámetros:
        texto = cadena de caracteres.
    Devuelve: 
        Un diccionario con las palabras que se encuentran en la cadena y su frecuencia.
    """
    texto = texto.split()
    diccionario = {}
    for i in texto:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario

    """Funcio que recibe el diccionario generado con la función anterior y devuelva
       una tupla con la palabra más repetida y su frecuencia.
    """

def palabramr(diccionario):
    palabra = ''
    frecuencia = 0
    for pal, frec in diccionario.items():
        if frec > frecuencia:
            palabra = pal
            frecuencia = frec
    return palabra, frecuencia

frase = str(input("Ingresa una frase:"))
print(contador1(frase))
print(palabramr(contador1(frase)))