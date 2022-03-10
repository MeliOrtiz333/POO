
class perro:

    def __init__(self,nombre):
        self.Nombre = nombre
        self.Hambre = 0
        self.isAlive = True

    @property
    def hambre(self):
        return self.Hambre

    def darHambre(self):
        if self.isAlive:
            self.Hambre += 2



    def alimentar(self,comida):
        if self.isAlive:
           self.Hambre -= comida


