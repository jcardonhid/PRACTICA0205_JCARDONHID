def acirculo(r):
    ac = 3.14159265*r**2
    return ac

def vcilindro(ac, h):
    vc = ac*h
    return vc

x = float(input("Ingresa el radio de un circulo para conocer su área:"))
y = float(input("Ingresa la altura del cilindro para conocer su volumen:"))

resultadoa = acirculo(x)
resultadov = vcilindro(resultadoa, y)

print("El área del circulo con radio:", x, "es:", round(resultadoa,2), "U^2")
print("El volumen del cilindro con radio:", x, "y altura:", y, "es:", round(resultadov,2), "U^3")
