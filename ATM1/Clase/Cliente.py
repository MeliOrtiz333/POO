class Persona:

    def __init__(self, nombre='', edad=None, curp=''):
        self.Nombre = nombre
        self.Edad = edad
        self.CURP = curp


    @property
    def Nombre(self):
       return self.Nombre

    @Nombre.setter
    def Nombre(self, NombreX):
        self.Nombre = NombreX

    @property
    def Edad(self):
        return self.Edad

    @Edad.setter
    def Edad(self, EdadX):
        self.Edad = EdadX

    @property
    def CURP(self):
        return self.CURP

    @CURP.setter
    def CURP(self,CURPX):
        self.CURP = CURPX




class Cuenta:

    def __init__(self,titular = '', NumCuenta=None, monto =0):
        self.Titular = titular
        self.NumeroDeCuenta = NumCuenta
        self.Monto = monto

    @property
    def Titular(self):
        return self.Titular

    @Titular.setter
    def Titular(self,TitularX):
        self.Titular = TitularX

    @property
    def NumeroDeCuenta(self):
        return self.NumeroDeCuenta

    @NumeroDeCuenta.setter
    def NumeroDeCuenta(self,NumDCx):
        self.NumeroDeCuenta = NumDCx

    @property
    def Monto(self):
        return self.Monto

    @Monto.setter
    def Monto(self,MontoX):
        self.Monto = MontoX


