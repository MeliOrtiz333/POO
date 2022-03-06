import random

class Embarcación():


    def __init__(self, nombre, tripulación,armamentopys, desplegables,coordenadas,cantidadC,velocidad):
        self.Nombre = nombre
        self.Tripulación = tripulación
        self.armamentoPyS = armamentopys
        self.despelegablesEx = desplegables
        self.coordenadas = coordenadas
        self.CantidadCombustible = cantidadC
        self.Velocidad = velocidad








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
        self.despelegablesEx = 100

        armamentoPrimario = int(input("¿Cuánto armamento primario hay?\n"))
        armamentoSecundario= int(input("¿Cuánto armamento secundario hay?\n"))
        EnergíaTotal = 1000
        disAP = armamentoPrimario - 1
        disAS = armamentoSecundario - 1
        energia = EnergíaTotal - 1
        armamento = armamentoPrimario + armamentoSecundario

        print("Su armamento total es: \n", armamento)
        print("su energía total es: \n",EnergíaTotal)

        disparo = input("¿Desea disparar? (S/N). Si desea desplegar el armamento extra presione <enter>\n\t")

        if disparo =="S":
            print("Usted ha disparado")
            print("Ahora su armamento primario es: ", disAP)
            print("Ahora su armamento secundario es: ",disAS)
            print("Su energía es:",energia)
            return
        elif disparo == "N":
            print("Usted NO ha disparado")
            print("Su armamento primario es: ", armamentoPrimario)
            print("Su armamento secundario es: ", armamentoSecundario)
            print("Su energía es:", EnergíaTotal)
            return
        else:
            print("No hay opción")



        disparoExtra = input("¿Desea usar los Desplegables extra? (S/N)\n\t")
        extra = 100
        disDE = extra -1

        if disparoExtra == "S":
            print("Usted ha disparado")
            print("Sus desplegues extras son: ", disDE)
            print("Su energía es: ", energia)

        elif disparoExtra == "N":
            print("Usted no disparó")

        else:
            print("Opción no válida")













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
        self.despelegablesEx = 100

        armamentoPrimario = int(input("¿Cuánto armamento primario hay?\n"))
        armamentoSecundario= int(input("¿Cuánto armamento secundario hay?\n"))
        EnergíaTotal = 1000
        disAP = armamentoPrimario - 1
        disAS = armamentoSecundario - 1
        energia = EnergíaTotal - 1
        armamento = armamentoPrimario + armamentoSecundario

        print("Su armamento total es: \n", armamento)
        print("su energía total es: \n",EnergíaTotal)

        disparo = input("¿Desea disparar? (S/N). Si desea desplegar el armamento extra presione <enter>\n\t")

        if disparo =="S":
            print("Usted ha disparado")
            print("Ahora su armamento primario es: ", disAP)
            print("Ahora su armamento secundario es: ",disAS)
            print("Su energía es:",energia)
            return
        elif disparo == "N":
            print("Usted NO ha disparado")
            print("Su armamento primario es: ", armamentoPrimario)
            print("Su armamento secundario es: ", armamentoSecundario)
            print("Su energía es:", EnergíaTotal)
            return
        else:
            print("No hay opción")



        disparoExtra = input("¿Desea usar los Desplegables extra? (S/N)\n\t")
        extra = 100
        disDE = extra -1

        if disparoExtra == "S":
            print("Usted ha disparado")
            print("Sus desplegues extras son: ", disDE)
            print("Su energía es: ", energia)

        elif disparoExtra == "N":
            print("Usted no disparó")

        else:
            print("Opción no válida")

















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
        self.despelegablesEx = 100

        armamentoPrimario = int(input("¿Cuánto armamento primario hay?\n"))
        armamentoSecundario= int(input("¿Cuánto armamento secundario hay?\n"))
        EnergíaTotal = 1000
        disAP = armamentoPrimario - 1
        disAS = armamentoSecundario - 1
        energia = EnergíaTotal - 1
        armamento = armamentoPrimario + armamentoSecundario

        print("Su armamento total es: \n", armamento)
        print("su energía total es: \n",EnergíaTotal)

        disparo = input("¿Desea disparar? (S/N)\n\t")

        if disparo =="S":
            print("Usted ha disparado")
            print("Ahora su armamento primario es: ", disAP)
            print("Ahora su armamento secundario es: ",disAS)
            print("Su energía es:",energia)
            return
        elif disparo == "N":
            print("Usted NO ha disparado")
            print("Su armamento primario es: ", armamentoPrimario)
            print("Su armamento secundario es: ", armamentoSecundario)
            print("Su energía es:", EnergíaTotal)
            return
        else:
            print("No hay opción")



        disparoExtra = input("Ya no tiene armamento Primario Y Secundario. ¿Desea usar los Desplegables extra? (S/N)\n\t")
        extra = 100
        disDE = extra -1

        if disparoExtra == "S":
           print("Usted ha disparado")
           print("Sus desplegues extras son: ", disDE)
           print("Su energía es: ", EnergíaTotal)

        elif disparoExtra == "N":
           print("Usted no disparó")

        else:
            print("Opción no válida")


