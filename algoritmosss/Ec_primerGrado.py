#Ecuación de primer grado

# ax + b = 0

#OBJETIVO - DEBE PEDIR LOS COEFICIENTES DE LA ECUACIÓN Y ENTREGAR LA SOLUCIÓN DE ESTA

# FORMULA SOLUCIÓN : (tener en cuenta que  a y b son constantes y x es una variable) x = - b/a

# definir valores
valor_a = float(input("Ingrese valor de a : "))
valor_b = float(input("Ingrese valor de b : "))
# solución 
if valor_a == 0:
    if valor_b == 0:
        print ("LA ECUACIÓN TIENE INFINITAS SOLUCIONES")
    else:
        print ("LA ECUACIÓN NO TIENE SOLUCIÓN")

else:
    x = -valor_b/valor_a
    print(f"La solución es {valor_a}x + {valor_b} = 0 es x = {x}")