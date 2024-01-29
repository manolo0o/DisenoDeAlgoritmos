# palabras palindromas.

def es_palindroma(palabra):
    p_invert = (str(palabra)[::-1]) 
    if palabra == p_invert:
        return True
    else:
        return False
    
palabra = input("INGRESE UNA PALABRA : ")
if es_palindroma(palabra):
    print("La palabra ingresada es PALINDROMA.")
else:
    print("La palabra no es PALINDROMA.")
    
# Altere el codigo para que reconozco frases palindromas.

def es_palindroma(frase):
    frase = frase.replace(" ", "")  # función para eliminar espacios
    frase_invertida = frase[::-1]
    
    if frase == frase_invertida:
        return True
    else:
        return False

frase = input("INGRESE UNA FRASE : ")
if es_palindroma(frase):
    print("La frase ingresada es PALINDROMA.")
else:
    print("La frase no es PALINDROMA.")
