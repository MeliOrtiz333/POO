from Circunferencia.Circunferencia import Circunferencia

Circunferencia = Circunferencia()

respuesta = 0

while respuesta != "S":
    print("-------------------------------")
    print("El nuevo radio es: ", Circunferencia.radio)
    print("Seleccione la opción que quiera")
    print("1.- De el nuevo radio con el que quiere trabajar")
    print("2.- Calculo del area con el nuevo radio")
    print("3.- Calculo del perimetro con el nuevo radio")
    print("Presione <S> para salir del programa")
    respuesta = input()

    if respuesta == "1":
        Circunferencia.radio = int(input("Ingrese el radio con el que quiere trabajar: \n"))
    elif respuesta == "2":

        print("El area de la circunferencia es:", Circunferencia.area())
        enter = input("Presione <enter> para continuar")
    elif respuesta == "3":
        print("El perimetro de la circunferencia es:", Circunferencia.perimetro())
        enter = input("Presione <enter> para continuar")
    elif respuesta == "S":
        print("Programa terminado")
        enter = input("Presione <enter> para salir")
