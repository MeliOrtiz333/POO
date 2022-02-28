from Clases.Cuadrilatero import Cuadrilatero

class Trapecio(Cuadrilatero):

    def __init__(self, lado1, lado2,altura,lado3,lado4):
        super().__init__(lado1, lado2,lado3,lado4)
        self.Altura = altura

    @property
    def alturaT(self):
        return self.alturaT

    @alturaT.setter
    def alturaT(self, h):
        self.Altura= h



    def areaTrapecio(self):
        areaTrapecio = ((self.Lado1 + self.Lado2) * self.Altura)/2
        print("\nEl area del trapecio es:   \t",areaTrapecio,"cm al cuadrado")