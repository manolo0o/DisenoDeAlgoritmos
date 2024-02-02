from sympy import symbols, solve

def buscar_soluciones():
    a, b, c = symbols('a b c', integer=True)
    objetivo = 100
    ecuacion = a**3 + b**3 + c**3 - objetivo

    soluciones = solve(ecuacion, (a, b, c))

    for solucion in soluciones:
        print(f"Solución encontrada: {solucion}")

buscar_soluciones()

