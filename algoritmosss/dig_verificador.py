
# dig verificadr

rol= input("ingrese su cc : ")
invertir = rol[::-1]
invertir = list(invertir)
multiplicar = []
cont = 2
dividiend = 11
for i in range(len(invertir)):
    multiplicar.append(int(invertir[i])*cont)
    cont = cont+ 1
    if (cont>7): cont = 2
    if (i==(len(invertir)-1)):
        result = sum(multiplicar)
        print(f"Resultado de la formula {result}")
        modul = result % dividiend
        print(f"resultado del modulo {modul}")
        validar = dividiend - modul
        print(f"resultado de la resta {validar}")
        print(f" digito verificador {rol}-{validar}")