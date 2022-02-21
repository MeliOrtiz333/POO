class Jugador:

    def __init__(self, nombre, monto, is_croupier=False):
        self.__Nombre = nombre
        self.__isCroupier = is_croupier
        self.Victorias = 0
        self.Derrotas = 0
        self.__Mano = []
        self.__Monto_Inicial = [monto]
        self.__Fichas_Actuales = monto
        self.__Apuesta = 0

    @property
    def nombre(self):
        return self.__Nombre

    @property
    def apuesta(self):
        return self.__Apuesta

    @property
    def depositos(self):
        return self.__Monto_Inicial

    @property
    def is_croupier(self):
        return self.__isCroupier

    @is_croupier.setter
    def is_croupier(self, val):
        self.__isCroupier = val

    @property
    def fichas(self):
        return self.__Fichas_Actuales

    @fichas.setter
    def fichas(self, nuevas_fichas):
        self.__Fichas_Actuales = nuevas_fichas

    @property
    def mano(self):
        mano = "Mano: ["
        for i in range(len(self.__Mano)):
            if i == 0 and self.__isCroupier:
                mano += " XX"
            else:
                mano += " " + self.__Mano[i]
        mano += " ] "
        if not self.__isCroupier:
            mano += "= "+str(self.contar())
        return mano

    @mano.setter
    def mano(self, carta):
        self.__Mano.append(carta)

    def contar(self):
        total = 0
        for i in range(len(self.__Mano)):
            v = self.__Mano[i]
            v = v.replace(v[len(v)-1], "")
            if v in "JQK":
                v = 10
            elif v == "A":
                v = 11 if total <= 10 else 1
            else:
                v = int(v)
            total += v
        return total

    def clear(self):
        self.__Mano = []

    def depositar(self, monto):
        try:
            monto = float(monto)
            if monto <= 0:
                print("¡El monto ingresado no es correcto!")
            else:
                self.__Monto_Inicial.append(monto)
                self.fichas += monto
        except ValueError:
            print("¡El monto ingresado no es correcto!")

    def place_bet(self):
        self.__Apuesta = 0
        print("Balance: ", self.fichas)
        a = input("¿Cuánto quieres apostar?")
        if a.isdigit():
            a = float(a)
            if self.fichas - a >= 0:
                self.__Apuesta = a
                self.fichas -= a
            else:
                print("¡No tienes fondos suficientes para esa apuesta!")
        else:
            print("¡El monto ingresado es incorrecto!")

