class Baraja:
    color = " "
    cantidad = 0
    nombre = " "

    def __init__(self,colorA, cantidadA, nombreA):
        self.color = colorA
        self.cantidad = cantidadA
        self.nombre = nombreA

    def carta(self, mensaje):
        print (mensaje)

    def cantidad(self, mensaje):
        print(mensaje)

    def color(self, mensaje):
        print(mensaje)

carta1 = Baraja("Roja", 10, "Corazones")
carta2 = Baraja("Roja", 10, "Diamantes")
carta3 = Baraja("Negra", 10, "Picas")
carta4 = Baraja("Negra", 10, "Tréboles")
carta5 = Baraja("Sin Color", 4, "Rey")
carta6 = Baraja("Sin Color", 4, "Reina")
carta7 = Baraja("Sin Color", 4, "Jota")

print('Carta 1', carta1.color, carta1.cantidad, carta1.nombre)
print('Carta 2', carta2.color, carta2.cantidad, carta2.nombre)
print('Carta 3', carta3.color, carta3.cantidad, carta3.nombre)
print('Carta 4', carta4.color, carta4.cantidad, carta4.nombre)
print('Carta 5', carta5.color, carta5.cantidad, carta5.nombre)
print('Carta 6', carta6.color, carta6.cantidad, carta6.nombre)
print('Carta 7', carta7.color, carta7.cantidad, carta7.nombre)

carta1.carta('La carta 1 es roja de corazones y hay 10 en la baraja de 52')
carta2.carta('La carta 2 es roja de diamantes y hay 10 en la baraja de 52')
carta3.carta('La carta 3 es negra de picas y hay 10 en la baraja de 52')
carta4.carta('La carta 4 es negra de tréboles y hay 10 en la baraja de 52')
carta5.carta('La carta 5 no tiene color específico, es el rey y hay 4 en la baraja de 52')
carta6.carta('La carta 5 no tiene color específico, es la reina y hay 4 en la baraja de 52')
carta5.carta('La carta 5 no tiene color específico, es jota y hay 4 en la baraja de 52')
