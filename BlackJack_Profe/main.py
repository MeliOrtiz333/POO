from Clases.Jugador import Jugador
from Clases.Deck import Baraja


def menu_de_juego(r, j1, c):
    print("------------------------------")
    print("Ronda", r, " - Apuesta:",j1.apuesta)
    print("\nCrupier:", c.nombre, "\n\t", c.mano)
    print("\nJugador:", j1.nombre, "\n\t", j1.mano)
    print("\n¿Qué quieres hacer?")
    print("h. Pedir carta")
    print("s. Quedarse")
    return input().lower()


def check_winner(j, c):
    c.is_croupier = False
    j_val = j.contar()
    c_val = c.contar()
    print("\n**********************************************************")
    if j_val > 21:
        print("¡Has perdido! - La casa gana automáticamente")
        j.Derrotas += 1
    elif c_val > 21 and j_val < 21:
        print("¡Has Ganado! - Felicitaciones")
        j.depositar(str(j.apuesta))
        j.Victorias += 1
    elif j_val > c_val:
        print("¡Has Ganado! - Felicitaciones x2")
        j.depositar(str(j.apuesta*2))
        j.Victorias += 1
    else:
        print("¡Has perdido!")
        j.Derrotas += 1
    print("Balance:", j.fichas)
    print("**********************************************************")
    print("Crupier:", c.nombre, "\n\t", c.mano)
    print("Jugador:", j.nombre, "\n\t", j.mano)
    return input("\n\n¿Quieres jugar otra ronda? s/n:").lower()


respuesta = "r"

n = input("¡Bienvenido a la mesa, Jugador!\nPor favor ingresa tu nombre: ")
d = int(input("Ingresa el monto de apertura en pesos: "))

jugador1 = Jugador(n, d)
croupier = Jugador("La Casa", 0, True)
baraja = Baraja()

ronda = 1
jugar = "s"

while jugar == "s":

    if baraja.cartas < 20:
        baraja.nueva_baraja()

    if jugador1.fichas <= 0:
        deposito = input("No dispones fondos para jugar, ¿quieres depositar más? s/n").lower()
        if deposito == "s":
            jugador1.depositar(input("¿Cuanto deseas depositar? Ingrese un monto en pesos: "))
        else:
            jugar = "n"
    else:
        jugador1.clear()
        croupier.clear()
        jugador1.place_bet()
        croupier.is_croupier = True
        jugador1.mano = baraja.pedir_carta()
        croupier.mano = baraja.pedir_carta()
        jugador1.mano = baraja.pedir_carta()
        croupier.mano = baraja.pedir_carta()
        accion = ""

        while accion != "s":
            if jugador1.contar() > 21:
                jugar = check_winner(jugador1, croupier)
                accion = "s"
            else:
                accion = menu_de_juego(ronda, jugador1, croupier)
                if accion == "h":
                    jugador1.mano = baraja.pedir_carta()
                elif accion == "s":
                    while croupier.contar() <= 16:
                        croupier.mano = baraja.pedir_carta()
                    jugar = check_winner(jugador1, croupier)
                else:
                    tmp = input("Esa opción no está en el menú. Presiona <enter> para escoger otra opción: ")
print("BALANCE FINAL")
print("\tVictorias:", jugador1.Victorias)
print("\tDerrotas:", jugador1.Derrotas)
print("Historial de depósitos:", jugador1.depositos)

