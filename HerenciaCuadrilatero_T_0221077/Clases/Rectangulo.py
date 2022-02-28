from Clases.Cuadrilatero import Cuadrilatero

class Rectangulo(Cuadrilatero):

    def __init__(self, lado1, lado2, lado3,lado4):
        super().__init__(lado1, lado2,lado3,lado4)


    def areaRectangulo(self):
        areaR = self.Lado1 * self.Lado2
        print("\nEl area del rectángulo es:   \t",areaR,"cm al cuadrado")