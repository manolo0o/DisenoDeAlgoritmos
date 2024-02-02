def es_primo(nro):
    if nro <2:
        return False
    for i in range(2,int(nro**0.5)+1):
        if nro % i == 0:
            return False
    return True

def obtener_primos_HN(n):
    primos = [i for i in range(2, n)if es_primo(i)]
    return primos

def obtener_factPrimos(nro):
    factores = []
    i = 2
    while i <= nro:
        if (nro %i) == 0:
            factores.append(i)
            nro=nro/i
        else:
            i = i + 1
    return factores

def suma_prim(nro_par):
    primos = obtener_primos_HN(nro_par)
    for i in primos:
        if nro_par - i in primos:
            print(f"{i} + {nro_par-i}")
            break
    
def primos_t7(n):
    primos_7 = [i for i in range(2,n) if es_primo(i) and i % 10 == 7]
    return primos_7

def suma_cuad_Pen1y1000():
    primos = obtener_primos_HN(1000)
    suma_cuadrados = sum (primo** 2 for primo in primos)
    return suma_cuadrados

def prod_primos_d7():
    primos_7 = [7, 17, 37, 47, 67, 71, 73, 79, 97]
    producto = 1
    for primo in primos_7:
        producto *= primo
    return producto
            
nro =int(input("ingrese su número :"))
if es_primo(nro):
    print(f"{nro} es primo.")
else: 
    print(f"{nro} es compuesto.")
    
n = int(input("cuantos primos : "))
for primo in obtener_primos_HN(n**2):
    print(primo)
    n -= 1
    if n == 0:
        break

m = int(input("Primos menos que: "))
for i in obtener_primos_HN(m):
    print(i)
    
m= int(input("Contar primos menores que: "))
cont_prim = sum(1 for i in range(2,m) if es_primo(i))
print(f"Hay {cont_prim} primos menores que {m}")

nro = int(input("Ingrese número: "))
for factor in obtener_factPrimos(nro):
    print(factor)
    
nro_par = int(input("Ingrese un número par: "))
if nro_par %2 == 0:
    suma_prim(nro_par)
else:
    print("El npumero ingresado no es par.")
    
print(f"Cantidad de primos menores que 10000 y terminan en 7: {len(primos_t7(10000))}")
print(f"Suma de cuadrados de primos entre 1 y 1000: {suma_cuad_Pen1y1000()}")
print(f"Producto de primos menores que 100 con dígito 7: {prod_primos_d7()}")
