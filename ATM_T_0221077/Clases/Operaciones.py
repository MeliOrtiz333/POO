class OP_Banco:

    tasa = 0.04

    @staticmethod
    def prestamo(cliente):
        p = input("Ingrese el monto que desea solicitar: ")

        if p.isdigit() and p != "":
            if float(p) > 0:
                cliente.cuenta.depositar(float(p))
                cliente.cuenta.deuda = float(p) * 1.04
                return
        print("El monto solicitado es incorrecto")

    @staticmethod
    def abono(cliente):
        print("El monto ingresado será descontado del balance de la deuda")
        print("Es necesario depositar previamente")
        p = input("Ingrese el monto que desea abonar: ")

        if p.isdigit() and p != "":
            if float(p) > 0 and float(p) < cliente.cuenta.monto:
                cliente.cuenta.retirar(float(p))
                cliente.cuenta.deuda -= float(p)
                return
        print("El monto solicitado es incorrecto")

    @staticmethod
    def intereses(cliente):
        cliente.cuenta.deuda = cliente.cuenta.deuda * (1 + OP_Banco.abono())

    @staticmethod
    def NuevaTasa():
        t =input("Ingrese la nueva tasa: ")
        if t.find("%") == len(t) - 1:
            t = float(t.replace("%", " ")) /100

        elif t.find(".") >= 0:
            t = float(t)
        else:
            t = float(t)/100

        OP_Banco.tasa = t
