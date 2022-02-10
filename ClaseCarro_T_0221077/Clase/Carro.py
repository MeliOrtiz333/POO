import random
class Carro:
    Marca = "Volkswagen"
    Color = "Rojo"
    Dueña = "Maria"
    Encendido = False
    Aceite = 50
    Placa = 0
    Cajuela_A= True


    def encenderAuto(self):
        self.Encendido = True
        print("\n\nUsted acaba de encender el auto.")
        self.__CajuelaC()


    def apagarAuto(self):
        if self.Encendido == False:

           self.Encendido = True

           self.__Cajuela_A()
           print("\n\nUsted puede cerrar la cajuela")


    def __Cajuela_A(self):
        print("Puede cerrar la cajuela cuando el auto esté apagado.")

    def __CajuelaC(self):
        print("La cajuela se ha cerrado automáticamente al prender el auto.")



    def ChecarAceite(self):
        if self.Aceite == 0:
            print("Se necesita más aceite")
        elif self.Aceite == 50:
            print("El aceite esta a la mitad")

        else:
            self.Aceite > 100
            print("Tiene suficiente aceite")

    def matricula(self):



        mayúsculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        números = "0123456789"
        longitudNum = 3
        longitudLet = 3


        cadenaNum = números
        cadenaLet = mayúsculas
        cad = random.sample(cadenaNum,longitudNum)
        cad2 = random.sample(cadenaLet,longitudLet)
        cuentaN = "".join(cad)
        cuentaL = "".join(cad2)

        print(cuentaN + " - " + cuentaL)
        self.Placa = cuentaN + " - " + cuentaL





















