import threading as th
import time



nom_us = input("Ingrese su nombre: \n")

r = 0
while r !="S":
    print("-------------------------------------")
    print("** Calculadora con temporizados de 3 segundos **")
    print("Seleccione la operación que desee hacer", nom_us)
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Multiplicación")
    print("4.- División")
    print("Presione <S> para salir")
    r = input()


    if r == "1":
        def suma():
           print("\nFin de la suma\n")


        num1 = int(input("De el primer a sumar\n"))
        num2 = int(input("De el segundo numero a sumar\n"))

        S = th.Timer(3.0, suma)
        S.start()
        time.sleep(3)
        sum = num1 + num2
        print("La suma es:  ", sum)
        S.cancel()


    elif r == "2":
        def resta():
            print("\nFin de la resta\n")


        num1 = int(input("De el primer a restar\n"))
        num2 = int(input("De el segundo numero a restar\n"))
        R = th.Timer(3.0, resta)
        R.start()
        time.sleep(3)
        res = num1 - num2
        print("La resta es:  ", res)
        R.cancel()



    elif r == "3":
        def multiplicación():
            print("\nFin de la multiplicación\n")


        num1 = int(input("De el primer a multiplicar\n"))
        num2 = int(input("De el segundo numero a multiplicar\n"))
        M = th.Timer(3.0, multiplicación)
        M.start()
        time.sleep(3)
        mult = num1 * num2
        print("La multiplicación es:  ", mult)
        M.cancel()


    elif r == "4":

        def division():
            print("\nFin de la división\n")


        num1 = int(input("De el primer a dividir\n"))
        num2 = int(input("De el segundo numero a dividir\n"))
        D = th.Timer(3.0, division)
        D.start()
        time.sleep(3)
        div = num1 / num2
        print("La division es:  ", div)
        D.cancel()


    elif r == "S":
        print("Usted ha salido")

    else:
        print("No hay opción")










