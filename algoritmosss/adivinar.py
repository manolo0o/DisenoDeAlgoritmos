#Escriba un programa que «piense» un número entre 0 y 100, y entregue pistas al usuario para que lo adivine.
#Fun randm

# from random import randrange
# n = randrange(101)

# n_correcto = n
# intento = 0

# while True:
#     try:
#         rta_usuario = int(input(f"(intento{intento+1}) ADIVINA EL NUMERO : "))
#         intento +=1 
        
#         if n_correcto > rta_usuario:
#             print (f"El número es mayor que {rta_usuario}")
#         elif n_correcto < rta_usuario:
#             print (f"El número es menor que {rta_usuario}")
#         elif rta_usuario == n_correcto:
#             print("¡¡ES CORRECTO!!")
#             print(f"Lo conseguiste en {intento+1} intentos.")
#             break
            
#     except ValueError:
#             print("Error: Ingresa un número válido.")

# Ahora invierta el juego, el pc debe adivinar el número

from random import randrange
import time
n_ct = int (input("Para que la maquina pueda adivinar, Ingrese un número del 1 al 100 : "))
intento = 0
inf = 1
sup = 100
print(" MAQUINA ADIVINA NÚMEROS ")

while True: 
    try:
        intento +=1
        r_machine = randrange(inf,sup + 1)
        
        print(f"Intento {intento} de la maquina: {r_machine}")
        time.sleep(2)
        
        if n_ct > r_machine:
            print(f"El número correcto es mayor que {r_machine}")
            inf = r_machine + 1
        elif n_ct < r_machine:
            print(f"El número correcto es menor que {r_machine}")
            sup = r_machine - 1
        elif n_ct == r_machine:
            print("¡¡ES CORRECTO!!")
            print(f"La maquina adivino en {intento+1} intentos.")
            break
    except ValueError:
            print("Error: Ingresa un número válido.")    
            