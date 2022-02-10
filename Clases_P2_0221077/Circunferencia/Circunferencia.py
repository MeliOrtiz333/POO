import math

class Circunferencia:
    __Radio = 0

    #Variable que se va a cambiar, inicia en 0.
    def __init__(self, radio =0):
        self.__Radio = radio

    @property
    def radio(self):
        return self.__Radio

    @radio.setter
    def radio(self, OtroRadio):
        self.__Radio = OtroRadio

    def area(self):
        return math.pi * self.radio * self.radio

    def perimetro(self):
        return 2 * math.pi * self.radio
