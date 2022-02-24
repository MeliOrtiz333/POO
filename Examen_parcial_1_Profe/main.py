from Clases.libros import Libro
import random

def submenu():
    print("Qué desea hacer?")
    print("1. Prestar")
    print("2. Devolver")
    return input("Opción: ")

libros = []
n = int(input("Cuantos libros quiere generar: "))
for i in range(n):
    libros.append(Libro("Libro "+str(i+1),"Autor "+str(i+1),random.randint(3,5)))

op = ""
while op != "s":
    print("Seleccione un libro")
    for i in range(len(libros)):
        print(str(i+1),") ",libros[i].Titulo)

    op = input("Libro: ")
    if(op == 's'):
        break

    l = int(input("Libro: ")) - 1

    if l < 0 or l >= len(libros):
        print("No es una opción valida")
    else:
        if submenu() == "1":
            libros[l].Prestamo()
        else:
            libros[l].Devolucion()
