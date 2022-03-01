import math

class Cuadrilatero:

    def __init__(self,lado1, lado2, lado3, lado4):
        self.Lado1 = lado1
        self.Lado2 = lado2
        self.Lado3 = lado3
        self.Lado4 = lado4



    def area(self):
        return "Formula no especificada"

    def perimetro(self):
        return self.Lado1 + self.Lado2 + self.Lado3 + self.Lado4





class Rectangulo(Cuadrilatero):

    def __init__(self,ladoA,ladoB):
        super().__init__(ladoA, ladoB,ladoA,ladoB)

    def area(self):
        return self.Lado1 * self.Lado2





class Cuadrado(Rectangulo):

    def __init__(self,lado):
        super().__init__(lado,lado)


class TrapecioA(Cuadrilatero):

    def __init__(self, ladoS, ladoI,altura):
        hipotenusa = math.sqrt(math.pow(((ladoI/2)-(ladoS/2)),2) + math.pow(altura,2))
        super().__init__(ladoS,ladoI,altura, hipotenusa)

    def area(self):
        return ((self.Lado1 + self.Lado2) * self.Lado3)/2

    def perimetro(self):
        return self.Lado1 + self.Lado2 + self.Lado4 + self.Lado4


