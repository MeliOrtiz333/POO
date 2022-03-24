#Aumenta 4% cada año y la casa vale 15,000,000. Después de 15 años ¿Cuánto va a valer?


def Aumento(v,lim, a=1):

    v = v * 1.04
    print("El valor de la casa después de  " + str(a) + " años es:\t" + str(v))
    a += 1
    if (a <= lim): Aumento(v, lim,a)

Aumento(15000000,15)


