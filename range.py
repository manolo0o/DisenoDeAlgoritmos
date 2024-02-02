# ¿Cuantos datos seran ingresados?
def dates_ing():
    try:    
        d_ing = int (input("¿Cuantos datos desea ingresar? : "))
    except ValueError:
        print("Error: Ingrese un número válido.")
        return
    dates = []
    
    for i in range(d_ing):
        try:
            dato = float(input(f"Ingrese el dato {i + 1}: "))
            dates.append(dato)
        except ValueError:
            print("Error: Ingrese un número válido.")
            return

    if dates:
        rng_datos = max(dates) - min(dates)
        print(f"El rango de los datos es: {rng_datos}")
    else:
        print("No se ingresaron datos.")

dates_ing()