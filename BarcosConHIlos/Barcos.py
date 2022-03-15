import random
import threading as th
import time




class Embarcación():


    def __init__(self, nombre, tripulación,armamentopys, desplegables,coordenadas,cantidadC,velocidad):
        self.Nombre = nombre
        self.Tripulación = tripulación
        self.armamentoPyS = armamentopys
        self.despelegablesEx = desplegables
        self.coordenadas = coordenadas
        self.CantidadCombustible = cantidadC
        self.Velocidad = velocidad


MunDis = 0
armamentoTotal = 100


hilos = {
    "hilo1": None,
    "hilo2":None


}

def hilo1_start():
    global MunDis, hilos
    MunDis += 1
    if MunDis < 100:
        hilos["hilo1"] = th.Timer(1, hilo1_start)
        hilos["hilo1"].start()

def hilo2_start():
    global armamentoTotal, hilos
    armamentoTotal -= 1
    if armamentoTotal > 0:
        hilos["hilo2"] = th.Timer(1,hilo2_start)
        hilos["hilo2"].start()


def detener_hilos():
    global hilos
    hilos["hilos1"].cancel()
    hilos["hilos2"].cancel()







class Acorazado(Embarcación):

    def __init__(self, nombre, tripulación,armamentopys, desplegables,coordenadas,cantidadC,velocidad):
        super().__init__( nombre, tripulación,armamentopys, desplegables,coordenadas,cantidadC,velocidad)

    def mostrarDatosAcorazado(self):
        nombreAcorazado = input("¿Cuál es el nombre del barco?\n\n")
        tripulacionAcorazado = input ("¿Cuál es el número de tripulantes de Acorazado?\n\n")
        print("------------------------------------------------")
        print("El nombre del Acorazado es: ", nombreAcorazado)
        print("La cantidad de tripulación en el Acorazado es: ", tripulacionAcorazado)
        print("El Acorazado está cargado con armamento, consulte la parte del armamento")
        print("La velocidad es 100 kh/h")


    def CantidadCombustibleAcorazado(self):
        litros = random.randint(0,10000)
        print("La cantidad de combustible es: ",litros, "litros")

    def coordenadasAcorazado(self):
       print("Las coordenadas actuales son: ( 109287, 756368 )")
       coordX = input("Digite la coordenada de orden x: \t")
       coordY = input("Digite la coordenada de orden y: \t")
       print("Las coordenadas actualizadas son: (",coordX, ", ",coordY, ")")


    def VelocidadAcorazado(self):
        velocidad = 100
        print("La velocidad es:\n\n\n", velocidad)

        vel = input("¿Desea aumentar <A>; disminuir <D> o mantener <M> la velocidad? (A/D/M)\n\t")
        aumentoV = velocidad + 100
        dismV = velocidad - 100



        if vel == "A":
            print("Se ha aumentado 100 km/h a la velocidad. Ahora su velocidad es: \t")
            return aumentoV

        elif vel == "M":
            print("La velocidad sigue constante\t")
            return velocidad

        elif vel == "D":
            print("La velocidad ha disminuido 100 km/h. Ahora su velocidad es:\t")
            return dismV

        else:
            print("Opción no válida\t")



    def MotoresAcorazado(self):

        motor = input("¿Desea apagar los motores? (S/N)\n\t")
        mapagado = "Motor apagado"
        maen = "Motor encendido"

        if motor == "S":
            print("Los motores han sido apagados\t")
            return mapagado

        elif motor == "N":
            print("Los motores están encendidos y siguen funcionando\t")
            return maen

        else:
            print("Opción no válida\t")



    def DispararArmaAcorazado(self):

        self.armamentoPyS = 0
        self.despelegablesEx = 0
        EnergíaTotal = 500

        print("El Acorazado solo tiene capacidad de 3 despliegues automaticos")
        disparo = input("¿Desea disparar? (S/N). Si desea desplegar el armamento extra presione <enter>\n\t")

        if disparo =="S":

          hilo1_start()
          hilo2_start()
          stop_mun = 0
          while stop_mun < 3:

            print("Se disparó\t\t"+ str(MunDis)+ "\t\tmuniciones, ahora su armamento es:\t\t"+str(armamentoTotal))

            time.sleep(15)
            stop_mun += 1


        elif disparo == "N":
            print("Usted NO ha disparado")

            return
        else:
            print("No hay opción")

        print("Presione <4> para parar el fuego")











class Destructor(Embarcación):

    def __init__(self, nombre, tripulación,armamentopys, desplegables,coordenadas,cantidadC,velocidad):
        super().__init__( nombre, tripulación,armamentopys, desplegables,coordenadas,cantidadC,velocidad)

    def mostrarDatosDestructor(self):
        nombreDestructor = input("¿Cuál es el nombre del barco?\n\n")
        tripulacionDestructor = input ("¿Cuál es el número de tripulantes del Destructor?\n\n")
        print("------------------------------------------------")
        print("El nombre del Destructor es: ", nombreDestructor)
        print("La cantidad de tripulación en el Destructor es: ", tripulacionDestructor)
        print("El Destructor está cargado con armamento, consulte la parte del armamento")
        print("La velocidad es 340 kh/h")


    def CantidadCombustibleDestructor(self):
        litros = random.randint(0,10760)
        print("La cantidad de combustible es: ",litros, "litros")

    def coordenadasDestructor(self):
       print("Las coordenadas actuales son: ( 109287, 756368 )")
       coordX = input("Digite la coordenada de orden x: \t")
       coordY = input("Digite la coordenada de orden y: \t")
       print("Las coordenadas actualizadas son: (",coordX, ", ",coordY, ")")


    def VelocidadDestructor(self):
        velocidad = 340
        print("La velocidad es:\n\n\n", velocidad)

        vel = input("¿Desea aumentar <A>; disminuir <D> o mantener <M> la velocidad? (A/D/M)\n\t")
        aumentoV = velocidad + 100
        dismV = velocidad - 100



        if vel == "A":
            print("Se ha aumentado 100 km/h a la velocidad. Ahora su velocidad es: \t")
            return aumentoV

        elif vel == "M":
            print("La velocidad sigue constante\t")
            return velocidad

        elif vel == "D":
            print("La velocidad ha disminuido 100 km/h. Ahora su velocidad es:\t")
            return dismV

        else:
            print("Opción no válida\t")



    def MotoresDestructor(self):

        motor = input("¿Desea apagar los motores? (S/N)\n\t")
        mapagado = "Motor apagado"
        maen = "Motor encendido"

        if motor == "S":
            print("Los motores han sido apagados\t")
            return mapagado

        elif motor == "N":
            print("Los motores están encendidos y siguen funcionando\t")
            return maen

        else:
            print("Opción no válida\t")



    def DispararArmaDestructor(self):

        self.armamentoPyS = 0
        self.despelegablesEx = 0
        EnergíaTotal= 600

        print("El Destructor solo tiene capacidad de 9 despliegues automaticos")
        disparo = input("¿Desea disparar? (S/N). Si desea desplegar el armamento extra presione <enter>\n\t")

        if disparo =="S":
          hilo1_start()
          hilo2_start()
          stop_mun = 0
          while stop_mun < 9:

            print("Se disparó\t\t"+ str(MunDis)+ "\t\tmuniciones, ahora su armamento es:\t\t"+str(armamentoTotal))

            time.sleep(15)
            stop_mun += 1


        elif disparo == "N":
            print("Usted NO ha disparado")

            return
        else:
            print("No hay opción")

        print("Presione <4> para parar el fuego")















class Crucero(Embarcación):

    def __init__(self, nombre, tripulación,armamentopys, desplegables,coordenadas,cantidadC,velocidad):
        super().__init__( nombre, tripulación,armamentopys, desplegables,coordenadas,cantidadC,velocidad)

    def mostrarDatosCrucero(self):
        nombreCrucero = input("¿Cuál es el nombre del barco?\n\n")
        tripulacionCrucero = input ("¿Cuál es el número de tripulantes del Crucero?\n\n")
        print("------------------------------------------------")
        print("El nombre del Crucero es: ", nombreCrucero)
        print("La cantidad de tripulación en el Crucero es: ", tripulacionCrucero)
        print("El Crucero está cargado con armamento, consulte la parte del armamento")
        print("La velocidad es 760 kh/h")


    def CantidadCombustibleCrucero(self):
        litros = random.randint(0,16784)
        print("La cantidad de combustible es: ",litros, "litros")

    def coordenadasCrucero(self):
       print("Las coordenadas actuales son: ( 109287, 756368 )")
       coordX = input("Digite la coordenada de orden x: \t")
       coordY = input("Digite la coordenada de orden y: \t")
       print("Las coordenadas actualizadas son: (",coordX, ", ",coordY, ")")


    def VelocidadCrucero(self):
        velocidad = 760
        print("La velocidad es:\n\n\n", velocidad)

        vel = input("¿Desea aumentar <A>; disminuir <D> o mantener <M> la velocidad? (A/D/M)\n\t")
        aumentoV = velocidad + 100
        dismV = velocidad - 100



        if vel == "A":
            print("Se ha aumentado 100 km/h a la velocidad. Ahora su velocidad es: \t")
            return aumentoV

        elif vel == "M":
            print("La velocidad sigue constante\t")
            return velocidad

        elif vel == "D":
            print("La velocidad ha disminuido 100 km/h. Ahora su velocidad es:\t")
            return dismV

        else:
            print("Opción no válida\t")



    def MotoresCrucero(self):

        motor = input("¿Desea apagar los motores? (S/N)\n\t")
        mapagado = "Motor apagado"
        maen = "Motor encendido"

        if motor == "S":
            print("Los motores han sido apagados\t")
            return mapagado

        elif motor == "N":
            print("Los motores están encendidos y siguen funcionando\t")
            return maen

        else:
            print("Opción no válida\t")




    def DispararArmaCrucero(self):

        self.armamentoPyS = 0
        self.despelegablesEx = 0
        EnergíaTotal= 300

        print("El Crucero solo tiene capacidad de 5 despliegues automaticos")
        disparo = input("¿Desea disparar? (S/N). Si desea desplegar el armamento extra presione <enter>\n\t")

        if disparo =="S":
          hilo1_start()
          hilo2_start()
          stop_mun = 0
          while stop_mun < 5:

            print("Se disparó\t\t"+ str(MunDis)+ "\t\tmuniciones, ahora su armamento es:\t\t"+str(armamentoTotal))

            time.sleep(2)
            stop_mun += 1


        elif disparo == "N":
            print("Usted NO ha disparado")

        else:
            print("No hay opción")

        print("Presione <4> para parar el fuego")




