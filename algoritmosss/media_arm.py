

def ingresar_numeros():

    n = int(input("Ingrese la cantidad de números que desea ingresar: "))
    while n <= 0:
        print("Por favor, ingrese un número mayor que 0.")
        n = int(input("Ingrese la cantidad de números que desea ingresar: "))

    numeros = []

    for i in range(1, n + 1):
        numero = float(input(f"Ingrese el número {i}: "))
        numeros.append(numero)

    return numeros

lista_de_numeros = ingresar_numeros()

def media_armonica(numeros):
    if len(numeros) == 0:
        return None
    
    suma_inversos = sum(1/x for x in numeros)

    media_arm = len(numeros) / suma_inversos
    return media_arm

n_ingresados = [float(x) for x in input("Ingrese los números separados por espacios: ").split()]
r_m_arm = media_armonica(n_ingresados)

if r_m_arm is not None:
    print("La media armonica es: ", r_m_arm)
else: 
    print("la lista de números esta vacia.")