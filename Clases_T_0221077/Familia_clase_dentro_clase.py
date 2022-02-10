class Familia:

    nombre = " "
    edad = 0
    integrante = " "
    Telefono = 0
    Email = " "
    Trabajo = " "



    def __init__(self,nombreA,edadA,integranteA):
        self.nombre = nombreA
        self.edad = edadA
        self.integrante = integranteA

    def nombre(self, mensaje):
        print(mensaje)

    def edad(self, mensaje):
        print(mensaje)

    def integrante(self, mensaje):
        print(mensaje)


Persona1 = Familia("Maria", 3, "Hija")
Persona2 = Familia("Jose", 32, "Padre")
Persona3 = Familia("Lulu", 30, "Madre")
Persona4 = Familia("Juan", 10, "Hijo")


print('Maria',Persona1.nombre,Persona1.edad, Persona1.integrante)
print('Jose',Persona2.nombre,Persona2.edad, Persona2.integrante)
print('Lulu',Persona3.nombre,Persona3.edad, Persona3.integrante)
print('Juan',Persona4.nombre,Persona4.edad, Persona4.integrante)

print('Se llama Maria, tiene 3 años y es la hija')
print('Se llama Jose, tiene 32 años y es el papá')
print('Se llama Lulu, tiene 30 años y es la mamá')
print('Se llama Juan, tiene 10 años y es el hijo')



class Datos:
    Telefono = 0
    Email = " "
    Trabajo = " "

    def __init__(self,telefonoA,EmailA,TrabajoA):
        self.Telefono = telefonoA
        self.Email = EmailA
        self.Trabajo = TrabajoA

    def Nombre(self,mensaje):
        print(mensaje)

    def Telefono(self, mensaje):
        print(mensaje)

    def Email(self, mensaje):
        print(mensaje)

    def Trabajo(self, mensaje):
        print(mensaje)



Persona1 = Datos(0, "no tiene ", "Nada")
Persona2 = Datos(5567832483, 32, "Contador")
Persona3 = Datos(553428192, 30, "Abogada")
Persona4 = Datos(0, "no tiene", "Estudiante")

print('Maria',Persona1.Telefono,Persona1.Email, Persona1.Trabajo )
print('Jose',Persona2.Telefono,Persona2.Email, Persona2.Trabajo )
print('Lulu',Persona3.Telefono,Persona3.Email, Persona3.Trabajo )
print('Juan',Persona4.Telefono,Persona4.Email, Persona4.Trabajo )


print('Maria, no tiene telefono y no trabaja')
print('Jose,su telefono es 5567832483 y es contador')
print('Lulu su telefono es 553428192 y es abogada')
print('Juan, no tiene telefono y es estudiante')