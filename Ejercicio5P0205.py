def cuadrado(lista0):
    lista1 = []
    for i in range(len(lista0)):
        x = lista0[i]**2
        lista1.append(x)
    return lista1

lista2=[]
datos=int(input("Ingresa una muestra de números enteros diferentes de 0 (Para salir presiona 0):\n"))
while datos != 0:
    lista2.append(datos)
    datos=int(input())
print("\nEste es el cuadrado de los números ingresados", cuadrado(lista2))