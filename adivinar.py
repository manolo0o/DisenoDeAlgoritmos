#Escriba un programa que «piense» un número entre 0 y 100, y entregue pistas al usuario para que lo adivine.
#Fun randm

from random import randrange
n = randrange(101)

n_correcto = n

while True:
    try:
        rta_usuario = int(input("ADIVINA EL NUMERO : "))
        if n_correcto > rta_usuario:
            print (f"El número es mayor que {rta_usuario}")
        elif n_correcto < rta_usuario:
            print (f"El número es menor que {rta_usuario}")
        elif rta_usuario == n_correcto:
            print("¡¡ES CORRECTO!!")
            break
            
    except ValueError:
            print("Error: Ingresa un número válido.")