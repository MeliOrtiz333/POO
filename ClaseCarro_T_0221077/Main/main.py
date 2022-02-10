from Clase.Carro import Carro
import random

coche = Carro()

print("\n\t\t\t\t\t\t\tEl auto es de:\n\t\t\t\t\t\t\t", coche.Dueña)
print("\n\t\t\t\t\t\t\tMarca y color: \n\t\t\t\t\t\t\t", coche.Marca, coche.Color)

print("-----------------------------------------------------------------------------------")
print("\n\t\t\tAntes de encender su auto, revise que todo esté en buen estado.\n\t\t\t")
print("-----------------------------------------------------------------------------------")
coche.ChecarAceite()
print("El aceite está: ", coche.Aceite)
print("-----------------------------------------------------------------------------------")


print("\nLa placa de su auto es: \n ")
coche.matricula()
print("-----------------------------------------------------------------------------------")

coche.encenderAuto()
print("\nEncender el auto: \n\t",coche.Encendido)
print("-----------------------------------------------------------------------------------")

coche. apagarAuto()
print("\nUsted acaba de apagar el auto.")
print("\nApagar auto: \n\t", coche.Encendido)
print("-----------------------------------------------------------------------------------")

