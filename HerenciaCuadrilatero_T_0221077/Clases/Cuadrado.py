from Clases.Cuadrilatero import Cuadrilatero

class Cuadrado(Cuadrilatero):

    def __init__(self, lado1, lado2, lado3,lado4):
        super().__init__(lado1, lado2, lado3,lado4)

    def areaCuadrado(self):
        areaCuadrado = self.Lado1 * self.Lado2 * self.Lado3 * self.Lado4
        print("\nEl area del cuadrado es:   \t",areaCuadrado,"cm al cuadrado")