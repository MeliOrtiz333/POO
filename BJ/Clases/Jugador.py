import random
from Clases.Baraja import Baraja


def menu2(): #Menu de apuesta
    print("No tiene crédito suficiente")
    print("¿Qué desea hacer?")
    print("1. Ingresar más dinero")
    print("2.  Salir del juego")


class Jugador:

    def __init__(self):
        self.Nombre = " "
        self.__Monto = 0.0
        self.baraja = Baraja()
        self.NombreBot = "croupier"  #Incluye el bot
        self.jugadorMano = []
        self.botMano = []
        self.valorjug = 0.0
        self.valorbot = 0.0
        self.apuestita = 0.0
        self.vic = 0
        self.der = 0




    @property
    def monto_monto(self):
        return self.__Monto


    def nombre(self): #Pedir que el nombre sea mayor a tres caracteres.
        a = input()
        while not a.isalpha() or len(a) < 3:
            print("Ingrese bien su nombre, sin caracteres especiales")
            a = input()

        self.Nombre = a



    def monto(self): #Tiene que ser valor mayor a 0
        b = float(input())
        while b <= 0:
            print("Es una cantidad inválida")
            b = float(input())

        self.__Monto = b



    def no_ingresos(self): #La apuesta debe ser menor a los fondos disponibles.
        if self.__Monto == 0:
            menu2()
            nou = input()
            if nou == "1":
                print("Ingrese la cantidad que quiere agregar: ")
                Jugador.monto(self)
                print("Su balance es de: ", self.__Monto)
            if nou == "2":
                quit()



    def apuesta(self): #Mas fichas y se vuelve a hacer la apuesta.
        b = float(input())
        while 0 > b or b > self.__Monto:
            print("Es una cantidad inválida")
            b = float(input())

        self.apuestita= b
        self.__Monto = self.__Monto - self.apuestita
        #Se reparten cartas pero antes se resta el monto de la apuesta.



    def mostrar(self): #Generar nuevo mazo.
        self.baraja.baraja()



    def manos(self): #Repartir uno y uno
        n = 0
        while n < 2:
            c = self.baraja.mazo.pop()
            self.jugadorMano.append(c)
            d = self.baraja.mazo.pop()
            self.botMano.append(d)
            n = n + 1


    def agregar(self, n): #Se vuelve a preguntar si quieres más cartas.
        self.baraja.pedir_carta(n)
        self.jugadorMano.append(self.baraja.agregar)






    def total(self): #Suma del valor de las cartas al jugador
        for i in self.jugadorMano:

            if i[0] == "2":
                self.valorjug = self.valorjug + 2
            elif i[0] == "3":
                self.valorjug = self.valorjug + 3
            elif i[0] == "4":
                self.valorjug = self.valorjug + 4
            elif i[0] == "5":
                self.valorjug = self.valorjug + 5
            elif i[0] == "6":
                self.valorjug = self.valorjug + 6
            elif i[0] == "7":
                self.valorjug = self.valorjug + 7
            elif i[0] == "8":
                self.valorjug = self.valorjug + 8
            elif i[0] == "9":
                self.valorjug = self.valorjug + 9
            elif i[0] == "1" and i[1] == "0":
                self.valorjug = self.valorjug + 10
            elif i[0] == "J" or i[0] == "Q" or i[0] == "K":
                self.valorjug = self.valorjug + 10
            elif i[0] == "A":
                aux = self.valorjug + 11 #Az de 11
                if aux <= 21:
                    self.valorjug = self.valorjug + 11
                else:
                    self.valorjug = self.valorjug + 1





    def totalbot(self): #Suma del puntaje del bot
        for i in self.botMano:

            if i[0] == "2":
                self.valorbot = self.valorbot + 2
            elif i[0] == "3":
                self.valorbot = self.valorbot + 3
            elif i[0] == "4":
                self.valorbot = self.valorbot + 4
            elif i[0] == "5":
                self.valorbot = self.valorbot + 5
            elif i[0] == "6":
                self.valorbot = self.valorbot + 6
            elif i[0] == "7":
                self.valorbot = self.valorbot + 7
            elif i[0] == "8":
                self.valorbot = self.valorbot + 8
            elif i[0] == "9":
                self.valorbot = self.valorbot + 9
            elif i[0] == "1" and i[1] =="0":
                self.valorbot = self.valorbot + 10
            elif i[0] == "J" or i[0] == "Q" or i[0] == "K":
                self.valorbot = self.valorbot + 10
            elif i[0] == "A":
                aux = self.valorbot + 11
                if aux <= 21:
                    self.valorbot = self.valorbot + 11
                else:
                    self.valorbot = self.valorbot + 1


#Jugador elige quedarse.

    def tomar_cartas(self): #El bot pide cartas hasta 17
        while self.valorbot < 17:
            self.baraja.cartuquis()
            self.botMano.append(self.baraja.agregar)
            self.valorbot = 0.0
            Jugador.totalbot(self)

    def recrear(self): #Se hace baraja nueva.
        self.baraja.recrearbaraja()


    def ganador(self):

        if self.valorjug > 21 and self.valorbot < 21:
            Jugador.perder(self) #Se pierde la apuesta
            self.der += 1

        elif self.valorbot > 21 and self.valorjug < 21:
            Jugador.ganar(self)
            print("Se devuelve lo que has apostado")
            self.vic += 1
            self.__Monto = self.__Monto + float(self.apuestita) + float(self.apuestita) #Se devuelve tu apuesta.

        elif self.valorbot == self.valorjug and self.valorbot < 21 and self.valorjug < 21:
            Jugador.empate(self)
            print("Nadie gana") #No se gana nada. Condicion del juego igual.


        elif self.valorjug == 21:
            Jugador.ganar(self)
            print("Se devuelve lo que has apostado x2")
            self.vic += 1
            self.__Monto = self.__Monto + (2*float(self.apuestita)) + float(self.apuestita) #Se agrega la apuesta y la otra parte.

        elif self.valorbot == 21:
            Jugador.perder(self)
            self.der += 1 #Pierde toda la apuesta el jugador


        elif self.valorbot < self.valorjug < 21:
            Jugador.ganar(self)
            self.vic += 1
            print("Se devuelve lo que has apostado")
            self.__Monto = self.__Monto + float(self.apuestita) + float(self.apuestita) #Se queda la apuesta intacta.


        elif self.valorjug < self.valorbot < 21:
            Jugador.perder(self)
            self.der += 1   #Pierde apuesta.


        elif self.valorjug > 21 and self.valorbot > 21:
            print("Perdieron") #No hay ganador

    def limpiar(self):   #Termina el juego
        self.jugadorMano.clear()
        self.botMano.clear()
        self.valorjug = 0.0
        self.valorbot = 0.0





# Desplegue del texto

    def ganar(self):
        print("\033[1;37;33m")
        print(" /$$                                                                               /$$          ")
        print("| $$                                                                              | $$          ")
        print("| $$$$$$$   /$$$$$$   /$$$$$$$        /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ ")
        print("| $$__  $$ |____  $$ /$$_____/       /$$__  $$ |____  $$| $$__  $$ |____  $$ /$$__  $$ /$$__  $$")
        print("| $$  \ $$  /$$$$$$$|  $$$$$$       | $$  \ $$  /$$$$$$$| $$  \ $$  /$$$$$$$| $$  | $$| $$  \ $$")
        print("| $$  | $$ /$$__  $$ \____  $$      | $$  | $$ /$$__  $$| $$  | $$ /$$__  $$| $$  | $$| $$  | $$")
        print("| $$  | $$|  $$$$$$$ /$$$$$$$/      |  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$/")
        print("|__/  |__/ \_______/|_______/        \____  $$ \_______/|__/  |__/ \_______/ \_______/ \______/ ")
        print("                                     /$$  \ $$                                                  ")
        print("                                    |  $$$$$$/                                                  ")
        print("                                     \______/                                                   ")
        print("\033[0m")

    def perder(self):
        print("\033[1;37;33m")
        print(" __                                                                      __  __        __           ")
        print("|  \                                                                    |  \|  \      |  \          ")
        print("| $$____    ______    _______         ______    ______    ______    ____| $$ \$$  ____| $$  ______  ")
        print("| $$    \  |      \  /       \       /      \  /      \  /      \  /      $$|  \ /      $$ /      \ ")
        print("| $$$$$$$\  \$$$$$$\|  $$$$$$$      |  $$$$$$\|  $$$$$$\|  $$$$$$\|  $$$$$$$| $$|  $$$$$$$|  $$$$$$\ ")
        print("| $$  | $$ /      $$ \$$    \       | $$  | $$| $$    $$| $$   \$$| $$  | $$| $$| $$  | $$| $$  | $$")
        print("| $$  | $$|  $$$$$$$ _\$$$$$$\      | $$__/ $$| $$$$$$$$| $$      | $$__| $$| $$| $$__| $$| $$__/ $$")
        print("| $$  | $$ \$$    $$|       $$      | $$    $$ \$$     \| $$       \$$    $$| $$ \$$    $$ \$$    $$")
        print(" \$$   \$$  \$$$$$$$ \$$$$$$$       | $$$$$$$   \$$$$$$$ \$$        \$$$$$$$ \$$  \$$$$$$$  \$$$$$$ ")
        print("                                    | $$                                                            ")
        print("                                    | $$                                                            ")
        print("                                     \$$                                                            ")
        print("\033[0m")

    def empate(self):
        print("   ___  ___ ___  ____    ____  ______    ___ ")
        print("  /  _]|   T   T|    \  /    T|      T  /  _]")
        print(" /  [_ | _   _ ||  o  )Y  o  ||      | /  [_ ")
        print("Y    _]|  \_/  ||   _/ |     |l_j  l_jY    _]")
        print("|   [_ |   |   ||  |   |  _  |  |  |  |   [_ ")
        print("|     T|   |   ||  |   |  |  |  |  |  |     T")
        print("l_____jl___j___jl__j   l__j__j  l__j  l_____j")
