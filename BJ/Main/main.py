from Clases.Jugador import Jugador

jugador1 = Jugador()

n = 0
alo = 0


def menu():
    print("          _____                    _____            _____                    _____                    _____                    _____                    _____                    _____                    _____          ")
    print("         /\    \                  /\    \          /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \                  /\    \         ")
    print("        /::\    \                /::\____\        /::\    \                /::\    \                /::\____\                /::\    \                /::\    \                /::\    \                /::\____\        ")
    print("       /::::\    \              /:::/    /       /::::\    \              /::::\    \              /:::/    /                \:::\    \              /::::\    \              /::::\    \              /:::/    /        ")
    print("      /::::::\    \            /:::/    /       /::::::\    \            /::::::\    \            /:::/    /                  \:::\    \            /::::::\    \            /::::::\    \            /:::/    /         ")
    print("     /:::/\:::\    \          /:::/    /       /:::/\:::\    \          /:::/\:::\    \          /:::/    /                    \:::\    \          /:::/\:::\    \          /:::/\:::\    \          /:::/    /          ")
    print("    /:::/__\:::\    \        /:::/    /       /:::/__\:::\    \        /:::/  \:::\    \        /:::/____/                      \:::\    \        /:::/__\:::\    \        /:::/  \:::\    \        /:::/____/           ")
    print("   /::::\   \:::\    \      /:::/    /       /::::\   \:::\    \      /:::/    \:::\    \      /::::\    \                      /::::\    \      /::::\   \:::\    \      /:::/    \:::\    \      /::::\    \           ")
    print("  /::::::\   \:::\    \    /:::/    /       /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\____\________    _____   /::::::\    \    /::::::\   \:::\    \    /:::/    / \:::\    \    /::::::\____\________  ")
    print(" /:::/\:::\   \:::\ ___\  /:::/    /       /:::/\:::\   \:::\    \  /:::/    /   \:::\    \  /:::/\:::::::::::\    \  /\    \ /:::/\:::\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\    \  /:::/\:::::::::::\    \ ")
    print("/:::/__\:::\   \:::|    |/:::/____/       /:::/  \:::\   \:::\____\/:::/____/     \:::\____\/:::/  |:::::::::::\____\/::\    /:::/  \:::\____\/:::/  \:::\   \:::\____\/:::/____/     \:::\____\/:::/  |:::::::::::\____\ ")
    print("\:::\   \:::\  /:::|____|\:::\    \       \::/    \:::\  /:::/    /\:::\    \      \::/    /\::/   |::|~~~|~~~~~     \:::\  /:::/    \::/    /\::/    \:::\  /:::/    /\:::\    \      \::/    /\::/   |::|~~~|~~~~~     ")
    print(" \:::\   \:::\/:::/    /  \:::\    \       \/____/ \:::\/:::/    /  \:::\    \      \/____/  \/____|::|   |           \:::\/:::/    / \/____/  \/____/ \:::\/:::/    /  \:::\    \      \/____/  \/____|::|   |          ")
    print("  \:::\   \::::::/    /    \:::\    \               \::::::/    /    \:::\    \                    |::|   |            \::::::/    /                    \::::::/    /    \:::\    \                    |::|   |          ")
    print("   \:::\   \::::/    /      \:::\    \               \::::/    /      \:::\    \                   |::|   |             \::::/    /                      \::::/    /      \:::\    \                   |::|   |          ")
    print("    \:::\  /:::/    /        \:::\    \              /:::/    /        \:::\    \                  |::|   |              \::/    /                       /:::/    /        \:::\    \                  |::|   |          ")
    print("     \:::\/:::/    /          \:::\    \            /:::/    /          \:::\    \                 |::|   |               \/____/                       /:::/    /          \:::\    \                 |::|   |          ")
    print("      \::::::/    /            \:::\    \          /:::/    /            \:::\    \                |::|   |                                            /:::/    /            \:::\    \                |::|   |          ")
    print("       \::::/    /              \:::\____\        /:::/    /              \:::\____\               \::|   |                                           /:::/    /              \:::\____\               \::|   |          ")
    print("        \::/____/                \::/    /        \::/    /                \::/    /                \:|   |                                           \::/    /                \::/    /                \:|   |          ")
    print("         ~~                       \/____/          \/____/                  \/____/                  \|___|                                            \/____/                  \/____/                  \|___|          ")


def finalizada(): #Salir
    print(".------..------..------..------..------..------..------. .------..------..------..------..------..------..------..------..------..------.")
    print("|P.--. ||A.--. ||R.--. ||T.--. ||I.--. ||D.--. ||A.--. | |F.--. ||I.--. ||N.--. ||A.--. ||L.--. ||I.--. ||Z.--. ||A.--. ||D.--. ||A.--. |")
    print("| :/\: || (\/) || :(): || :/\: || (\/) || :/\: || (\/) | | :(): || (\/) || :(): || (\/) || :/\: || (\/) || :(): || (\/) || :/\: || (\/) |")
    print("| (__) || :\/: || ()() || (__) || :\/: || (__) || :\/: | | ()() || :\/: || ()() || :\/: || (__) || :\/: || ()() || :\/: || (__) || :\/: |")
    print("| '--'P|| '--'A|| '--'R|| '--'T|| '--'I|| '--'D|| '--'A| | '--'F|| '--'I|| '--'N|| '--'A|| '--'L|| '--'I|| '--'Z|| '--'A|| '--'D|| '--'A|")
    print("`------'`------'`------'`------'`------'`------'`------' `------'`------'`------'`------'`------'`------'`------'`------'`------'`------'")
    print("\n\n")
    print("Gracias por jugar,", jugador1.Nombre)
    print("Sus victorias fueron: ", jugador1.vic)
    print("Sus derrotas fueron: ", jugador1.der)


def nombre(): #Pedir nombre
    print("\n???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????? ")
    print("\033[1;37;33m ??? Postor, por favor ingrese su nombre: ???")
    print("?????????")
    jugador1.nombre()
    print("\033[0m????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????\n")


def dinero(): #Pedir apuesta
    print("\033[1;37;33m??? Bienvenido/a ", jugador1.Nombre, ", ingrese el dinero que se quiere importar en el juego ???")
    print("?????????")
    jugador1.monto()
    print("\033[0m????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????\n")


def datos_juego(): #Cartas del bot, jugador y valor de puntos.
    jugador1.manos()

    print("???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
    print("??????                                         ??????")
    print("??????\033[1;31;40mCartas croupier: ['", jugador1.botMano[0], "', '[X]']         \033[0m??????")
    print("\033[0m??????                                         ??????")
    print("??????                                         ??????")
    print("??????\033[1;32;40mTus cartas: ", jugador1.jugadorMano, "              \033[0m??????")
    jugador1.total()
    print("??????\033[1;32;40mSu puntaje es: ", jugador1.valorjug, "                    \033[0m??????")
    print("??????                                         ??????")
    print("??????                                         ??????")
    print("???????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")


def pedir_cartas(): #Resumen para el jugador.
    jugador1.agregar(alo)
    jugador1.valorjug = 0.0
    jugador1.total()
    print("????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
    print("??????                                                                ??????")
    print("??????                                                                ??????")
    print("??????\033[1;32;40mTus cartas: ", jugador1.jugadorMano, "                              \033[0m??????")
    print("??????\033[1;32;40mSu puntaje es: ", jugador1.valorjug, "                                           \033[0m??????")
    print("??????                                                                ??????")
    print("??????                                                                ??????")
    print("????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")


def datos_ganador():
    print("\n?????????????????????????????????????????????????????????????????????????????????????????????????????? ")
    jugador1.ganador()
    print("\n?????????????????????????????????????????????????????????????????????????????????????????????????????? ")
    print("Cartas de croupier: ", jugador1.botMano)
    print("Su puntaje es: ", jugador1.valorbot)
    print("Tus cartas: ", jugador1.jugadorMano)
    print("Su puntaje es: ", jugador1.valorjug)
    print("\n?????????????????????????????????????????????????????????????????????????????????????????????????????? ")

# Empieza


menu()
nombre()
dinero()
print("???????????????????????? ????????????????????: ???????????????????????????????????? ????????")
jugador1.mostrar()
while n != "no":
    print("\n????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????????")
    jugador1.recrear()
    print("balance: ", jugador1.monto_monto)
    jugador1.no_ingresos()
    print("\033[1;37;33mIngresa cu??nto quieres apostar en esta ronda: ")
    jugador1.apuesta()

    print("\033[0mIngresa (s??) para iniciar la ronda")
    r = input()

    if r == "S??" or r == "S??" or r == "si" or r == "SI" or r == "s??":
        print("\n")
        print("-------------------------------------------------------------")
        print("Su apuesta es de: $", jugador1.apuestita, "[????$????(??????????????)????$????]")
        datos_juego()
        while alo != "No" and alo != "NO" and alo != "no":
            print("??Desea pedir otra tarjeta?")
            alo = input()
            if alo == "s??" or alo == "si" or alo == "S??" or alo == "Si" or alo == "S??" or alo == "S??":
                pedir_cartas()

        jugador1.totalbot()
        jugador1.tomar_cartas()
        datos_ganador()
        print("\n??Desea seguir jugando? (s??/no)")
        n = input()
        if n == "s??" or n == "si" or n == "S??" or n == "Si" or n == "S??" or n == "S??":
            jugador1.limpiar()
            alo = 0
finalizada()
