def CalcularT(minPista):
    return (((minPista -20) ** 3)/ 100) +10


def CalcularDesgaste(Tiempo,tentreCarreras):
    desgaste = tentreCarreras * CalcularT(Tiempo)
    print(desgaste)
    if desgaste < 0:
        desgaste = 0
    return desgaste



def desgaste(durabilidad = 3000, tiempo = 0, TentreCarreras = 1):
    tiempo += TentreCarreras
    durabilidad -= CalcularDesgaste(tiempo,TentreCarreras)
    print("-----------------------------------------------------")
    print("Tiempo transcurrido", tiempo,"minutos")
    print("Durabilidad restante", durabilidad)
    if durabilidad < 1000:
        print("Llanta debe cambiarse")
    else:
        desgaste(durabilidad, tiempo)

desgaste()