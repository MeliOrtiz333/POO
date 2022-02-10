class Figura:
    lados = 0
    perimetro = 0
    area = 0

    
    def __init__(self,ladosx,perimetrox, areax):
        self.lados = ladosx
        self.perimetro = perimetrox
        self.area = areax


    def nombre(self,mensaje):
        print(mensaje)

    def perimetro(self, mensaje):
        print(mensaje)

    def area(self, mensaje):
        print(mensaje)



Triangulo = Figura(3,24, 67)
Cuadrado = Figura (4,75, 90)
Rectángulo = Figura (4,90, 100)
Hexágono = Figura (6, 60, 97)

print('Triangulo', Triangulo.lados,Triangulo.perimetro, Triangulo.area)
print('Cuadrado', Cuadrado.lados,Cuadrado.perimetro,Cuadrado.area)
print('Rectángulo', Rectángulo.lados,Rectángulo.perimetro, Rectángulo.area)
print('Hexagono', Hexágono.lados,Hexágono.perimetro,Hexágono.area)

Triangulo.nombre('Un triangulo tiene 3 lados, Su perimetro es de 24 cm, Su area es de 67 cm cuadrados')
Cuadrado.nombre('Un cuadrado tiene 4 lados, Su perimetro de 75 cm, Su area de 90 cm cuadrados')
Rectángulo.nombre('Un rectángulo tiene 4 lados, Su perimetro de 90 cm, Su perimetro de 90 cm, Su area de 100 cm')
Hexágono.nombre('Un hexágono tiene 6 lados,Su perimetro de 60 cm, Su area de 97 cm cuadrados')




