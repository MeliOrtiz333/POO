import random


class Baraja:

    def __init__(self):
        self.__deck = []
        self.nueva_baraja()

    def barajar(self):
        random.shuffle(self.__deck)

    def nueva_baraja(self):
        self.__deck = []
        palos = ["♥", "♦", "♣", "♠"]
        for i in range(len(palos)):
            self.__deck.append("A"+palos[i])
            for j in range(8):
                self.__deck.append(str(j+2)+palos[i])
            self.__deck.append("J"+palos[i])
            self.__deck.append("Q"+palos[i])
            self.__deck.append("K"+palos[i])
        self.barajar()

    @property
    def cartas(self):
        return len(self.__deck)

    def pedir_carta(self):
        carta = self.__deck[len(self.__deck)-1]
        self.__deck.remove(carta)
        return carta
