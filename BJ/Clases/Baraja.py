import random
class Baraja:

    def __init__(self):
        self.agregar = []
        self.mazo = []
        self.cartas = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K", "Q"] # Del 2 al 10 tienen su valor natural
        self.palos = ["♤", "♧", "♥", "♦"] #Valen 10, pero el az toma valor 1 u 11

    def baraja(self): # Se crea la baraja y se barajea automaticamente.

        for i in self.palos:
            for j in self.cartas:
                self.mazo.append(j + i)
        random.shuffle(self.mazo)

    def cartuquis(self): #Se agrega la carta a la computadora o al mazo.
        self.agregar = self.mazo.pop()

    def pedir_carta(self, n): #Agarra la carta y se la pasa al jugador o a la computadora.
        if n == "sí" or n == "si" or n == "Sí" or n == "Si" or n == "SÍ" or n == "SÍ":
            Baraja.cartuquis(self)

    def recrearbaraja(self): #Se crea nueva baraja.
        if len(self.mazo) < 15:
            self.mazo.clear()
            Baraja.baraja(self)
