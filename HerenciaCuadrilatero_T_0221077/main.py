from Clases.Cuadrilatero import Cuadrilatero
from Clases.Cuadrado import Cuadrado
from Clases.Rectangulo import Rectangulo
from Clases.Trapecio import Trapecio


print("\nLos lados de un cuadrilatero cualquiera es: lado 1 = 2cm, lado 2 = 4cm, lado 3 = 4cm\t")
cuadrilateroX = Cuadrilatero(2,4,4,6)
cuadrilateroX.area()
print("-------------------------------------------------------------------------------------------")




print("\nLos lados de un cuadrado es: lado 1 = 2cm, lado 2 = 2cm, lado 3 = 2cm\t")
cuadradoX = Cuadrado(2,2,2,2)
cuadradoX.areaCuadrado()
print("-------------------------------------------------------------------------------------------")




print("\nLos lados de un rectangulo es cualquiera es: base = 10cm, altura = 8cm\t")
rectanguloX = Rectangulo(10,8,1,1)
rectanguloX.areaRectangulo()
print("-------------------------------------------------------------------------------------------")



print("\nLos lados de un trapecio cualquiera es: lado 1 = 20cm, lado 2 = 14cm, altura = 4cm\t")
trapecioX = Trapecio(20,14,5,1,1)
trapecioX.areaTrapecio()
print("-------------------------------------------------------------------------------------------")