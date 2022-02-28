class Cuadrilatero:

    def __init__(self, lado1, lado2, lado3,lado4):
        self.Lado1 = lado1
        self.Lado2 = lado2
        self.Lado3 = lado3
        self.Lado4 = lado4




    @property
    def LadoA(self):
        return self.Lado1

    @LadoA.setter
    def LadoA(self,l1):
        self.Lado1 = l1

    @property
    def LadoB(self):
        return self.Lado2

    @LadoB.setter
    def LadoB(self, l2):
        self.Lado2 = l2

    @property
    def LadoC(self):
        return self.Lado3

    @LadoC.setter
    def LadoC(self, l3):
        self.Lado3 = l3

    @property
    def LadoD(self):
        return self.Lado4

    @LadoD.setter
    def LadoD(self, l4):
        self.Lado4 = l4

    def area(self):
        area= self.Lado1 * self.Lado2 * self.Lado3 * self.Lado4
        print("\nEl area del cuadrilatero es: ",area,"cm al cuadrado")

