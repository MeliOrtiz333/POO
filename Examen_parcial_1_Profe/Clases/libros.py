class Libro:

    def __init__(self,titulo,autor,inv):
        self.Titulo = titulo
        self.Autor = autor
        self.__Inventario = inv
        self.__Prestados = 0

    @property
    def inventario(self):
        return self.__Inventario

    @inventario.setter
    def inventario(self,inv):
        self.__Inventario = inv

    @property
    def prestados(self):
        return self.__Prestados

    @prestados.setter
    def prestados(self, pre):
        self.__Prestados = pre

    def Prestamo(self):
        if self.prestados < self.inventario:
            self.prestados += 1
            print("Se ha prestado el libro")
        else:
            print("No tenemos inventario disponible")

    def Devolucion(self):
        if self.prestados > 0:
            self.prestados -= 1
            print("Se ha devuelto el libro con éxito")
        else:
            print("Nada que devolver")