
AH = open('VisitasAlHospital.txt', 'r')


#Mostrar datos de los departamentos
archivo_hospital = {
    'Otorrinolaringologia':(AH.readlines(1)),
    'Oftalmologia':(AH.readlines(2)),
    'Hematologia':(AH.readlines(3)),
    'Urologia': (AH.readlines(4)),
    'Nefrologia':(AH.readlines(5)),
    'Ortopedia':(AH.readlines(6)),
    'Cirugia Plastica': (AH.readlines(7)),
    'Dermatologia': (AH.readlines(8)),
    'Geriatria':(AH.readlines(9)),
    'Laboratorio':(AH.readlines(10)),
    'Radiologia e Imagenologia':(AH.readlines(11)),
    'Consulta Externa':(AH.readlines(12)),
    'Medicina Preventiva':(AH.readlines(13)),
    'Banco de Sangre':(AH.readlines(14)),
    'Neurologia y Neurocirugia':(AH.readlines(15))

}


print(archivo_hospital)


paciente = {

    'Nombre del paciente:': None,
    'Edad': None,
    'Padecimiento':None,
    'Número de paciente': None
}

def pedirnombre():
    nombre_P = input("¿Cuál es el nombre del paciente?")
    print("El nombre que introdujo fue:", nombre_P)