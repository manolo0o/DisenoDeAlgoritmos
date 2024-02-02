def esnrsprs(nrs):
    if nrs < 2:
        return False
    for i in range(2,int(nrs**0.5)+1):
        if nrs %i == 0:
            return False
    return True
    
def nrsprs():
    nrs = int(input("Ingrese un numero : "))
    if esnrsprs(nrs):
        print("EL numero es primo")
    else:
        print("Es compuesto")
        