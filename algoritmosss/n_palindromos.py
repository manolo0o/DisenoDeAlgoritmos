

def es_palindromo(numero):
    numero_invertido = int(str(numero)[::-1])  # Invertir el número convirtiéndolo a cadena, invirtiendo y convirtiendo a entero
    if numero == numero_invertido:
        return True
    else:
        return False

numero = int(input("Ingrese un número: "))

if es_palindromo(numero):
    print("El número ingresado es palíndromo.")
else:
    print("El número ingresado no es palíndromo.")