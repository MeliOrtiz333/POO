from Clase.Rectangulo import  Rectangulo



p = input("Ingrese la altura y anchura de la pared (en metros), separados por coma(,): ").split(",")
pared = Rectangulo(p, "Pared")

v = input("Ingrese la altura y anchura de la ventana (en metros), separados por coma(,): ").split(",")
ventana = Rectangulo(v, "Ventana")

area_total = pared.area()-ventana.area()

print("Tardarías (", area_total*10, "minutos) pintar toda la pared.")