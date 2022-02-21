from Clase.Cliente import Persona
from Clase.Cliente import Cuenta
import random

Persona.Nombre = input("\t\nEscriba su nombre completo:\n")
print("El nombre que dio es:\n\t ", Persona.Nombre)



Persona.Edad = int(input("Ingrese su edad:"))
print("La edad que dio es: ", Persona.Edad)
if Persona.Edad >= 18:
    print("Es mayor de edad\n\t")
else:
    print("La persona es menor de edad\n\t")



Persona.CURP = input("Ingrese su CURP \n\t")

caracteres = len(Persona.CURP)


if Persona.CURP.isalnum() == True:
    if caracteres < 8:
        print("El CURP tiene menos caracteres de los requeridos, debe tener 8 caracteres alfanúmericos\n\t")
    elif caracteres > 8:
        print("EL CURP tiene caracteres de más\n\t")
    else:
        print("El CURP que ingreso es: \n\t", Persona.CURP)

else:
    print("Ha ingresado de manera incorrecta el CURP\n\t")






Cuenta.NumeroDeCuenta = print("El número de cuenta es: \n\n",)

mayúsculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
minúsculas = "abcdefghijklmnopqrstuvwxyz"
números = "0123456789"
longitud = 8

cadena1 = minúsculas + mayúsculas + números
cadena2 = random.sample(cadena1,longitud)
cuenta = "".join(cadena2)
print(cuenta)


respuesta = 0
while respuesta != "S":
    print("-------------------------------")
    print("Bienvenido a tu estado de cuenta:  \n \t", Persona.Nombre)
    print("Su número de cuenta es de cuenta es:  \n \t",cuenta)
    print("Seleccione la opción que desee\n\t")
    print("1.- Si desea ver el estado actual de su cuenta\n\t")
    print("2.- Si desea depositar\n\t")
    print("3.- Si desea retirar\n\t")
    print("Presione <S> para salir del estado de cuenta")
    respuesta = input()

    if respuesta == "1":

        Cuenta.Monto = print("El estado actual de su cuenta es: \n\t")
        números2 = "0123456789"
        cadena = números2
        longitud2 = 6
        cantidad = random.sample(cadena, longitud2)
        monto = "".join(cantidad)
        print(monto)


    elif respuesta == "2":

        depósito = int(input("Ingrese la cantidad que desea depositar: \n\t"))

        while(depósito < 0):
            print("El monto ingresado es negativo intente de nuevo")

            depósito = int(input("Ingrese la cantidad que desea depositar: \n\t"))
        print("El monto ingresado es: ", depósito)


        Cuenta.MontoD = int(monto) + depósito
        print("El monto final es: \n\t")
        print((Cuenta.MontoD))


    elif respuesta == "3":

        retiro = int(input("Ingrese la cantidad que desea retirar: \n\t"))
        while (retiro > int(monto)):
            print("No es posible retirar esa cantidad, ya que no existe, intente otra vez")

            retiro = int(input("Ingrese la cantidad que desea retirar: \n\t"))
        print("El monto ingresado es: ", retiro)

        Cuenta.MontoR = int(monto) - retiro
        print("El monto final es: \n\t")
        print((Cuenta.MontoR))



    elif respuesta == "S":
        print("Gracias por revisar su cuenta")
        enter = input("Presione <enter> para salir")


