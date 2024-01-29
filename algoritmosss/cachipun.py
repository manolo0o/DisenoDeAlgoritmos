# CACHIPUN (PIEDRA , PAPEL O TIJERA)


def cachipun(jugador1, jugador2, eleccion1, eleccion2):
    if eleccion1 == eleccion2:
        print("empate")
    elif (
        (eleccion1 == "piedra" and eleccion2 == "tijera") or
        (eleccion1 == "tijera" and eleccion2 == "papel") or
        (eleccion1 == "papel" and eleccion2 == "piedra")
    ):
        return f"{jugador1} GANA"
    else:
        return f"{jugador2} GANA"
    
max_rondas= 3

jugador1 = input("ingrese nombre del jugador 1 : ")
jugador2 = input("ingrese nombre del jugador 2 : ")

marcador_jugador1 = 0
marcador_jugador2 = 0

for ronda in range(1, max_rondas + 1):
    print(f"\nRonda {ronda}")

    eleccion1 = input(f"{jugador1}, elige piedra, papel o tijera: ").lower()
    while eleccion1 not in ["piedra", "papel", "tijera"]:
        print("OPCIÓN NO VÁLIDA, INGRESE piedra, papel o tijera")
        eleccion1 = input(f"{jugador1}, elige piedra, papel o tijera: ").lower()

    eleccion2 = input(f"{jugador2}, elige piedra, papel o tijera: ").lower()
    while eleccion2 not in ["piedra", "papel", "tijera"]:
        print("OPCIÓN NO VÁLIDA, INGRESE piedra, papel o tijera")
        eleccion2 = input(f"{jugador2}, elige piedra, papel o tijera: ").lower()

    resultado = cachipun(jugador1, jugador2, eleccion1, eleccion2)
    print(resultado)
    
    if "GANA" in resultado:
        if resultado.startswith(jugador1):
            marcador_jugador1 += 1
        else:
            marcador_jugador2 += 1

    print(f"Marcador: {jugador1} {marcador_jugador1} - {jugador2} {marcador_jugador2}")

print("\nMarcador Final:")
print(f"{jugador1}: {marcador_jugador1} - {jugador2}: {marcador_jugador2}")

if marcador_jugador1 > marcador_jugador2:
    print(f"\n¡{jugador1} es el ganador!")
elif marcador_jugador1 < marcador_jugador2:
    print(f"\n¡{jugador2} es el ganador!")
else:
    print("\n¡El juego terminó en empate!")


print("FIN DEL GAME")