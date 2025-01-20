def med_lis(lista0):
    """La función med_lis recibe una muestra de números en una lista y devuelva su media.
       la variable media ejecuta la media de los valores de la lista.
    """
    media = sum(lista0)/len(lista0)
    return media

lista1=[]
datos=int(input("Ingresa una muestra de números enteros diferentes de 0 (Para salir presiona 0):\n"))
while datos != 0:
    lista1.append(datos)
    datos=int(input())
print("\nEsta es la media de la muestra ingresada:", round(med_lis(lista1),2))