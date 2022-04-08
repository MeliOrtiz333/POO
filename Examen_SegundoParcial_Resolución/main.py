from ast import literal_eval
import json


archivo = open("VisitasAlHospital.txt", "r")
visitas = archivo.readlines()
archivo.close()

#Se tiene un arreglo de arreglos.
#Imprimir los datos.

departamentos = {}
for v in visitas:
    v = v.split("=")
    departamentos[v[0]] = literal_eval(v[1])

print(departamentos)

#Arreglo vacio de pacientes.
pacientes ={}
anidados = {}



def iterar_grupo(arreglo,departamento):

    for codigo in arreglo:
        
        if type(codigo) == int:
            if codigo in pacientes.keys():
                if departamento in pacientes[codigo].keys():
                    pacientes[codigo][departamento] += 1

                else:
                    pacientes[codigo][departamento] = 1

            else:
                pacientes[codigo] ={}
                pacientes[codigo][departamento] = 1


        else:
            if departamento in anidados.keys():        #Easter Egg (extra).
                anidados[departamento] += 1
            else:
                anidados[departamento] = 1
                iterar_grupo(codigo,departamento)


for k in departamentos.keys():
    iterar_grupo(departamentos[k],k)

print(pacientes)
print(anidados)

#Identificar cuantas veces fue el paciente y a que zona.
file = open("analisis.json", "w")
file.write(json.dumps(pacientes, indent=4))
file.close()



