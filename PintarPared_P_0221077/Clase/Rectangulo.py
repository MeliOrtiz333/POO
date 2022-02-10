class Rectangulo:
    largo = 0.0
    ancho = 0.0

    def __init__(self, medidas,nombre):
        self.largo = float(medidas[0])
        self.ancho = float(medidas[1])
        print("Registrando", nombre, " con medidas\n\tLargo:", self.largo, "\n\tAncho:", self.ancho)

    def area(self):
        return self.largo * self.ancho
