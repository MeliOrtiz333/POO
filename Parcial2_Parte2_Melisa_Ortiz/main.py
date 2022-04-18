# 1.- Crear clase cuenta.

class Cuenta():
    def __init__(self,numdeC, nombre, balance):
        self.NumerodeCuenta = numdeC
        self.Nombre = nombre
        self.Balance = balance


# 2.-Hacer la busqueda en el documento.

def busqueda(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return True

    return False

# 3.- Imprimir el arreglo.

def imprimirArreglo(arreglo):
    for i in range(0, len(arreglo)):
        print(arreglo[i])

# 4 .- Leer archivo y crear un arreglo bidimensional.

def iArchivo(archivo):
    arregloB = []
    with open(archivo, 'r') as file:
        for line in file.readlines():
            arregloB.append(line.split(' '))

    return arregloB

# 5.- Hacer la conversión a pesos mexicanos.

def convertiraPesos(arregloB):
    libras = 26.35
    dolares = 20.17
    yenes = 0.16

    for i in range(0, len(arregloB)):
        if arregloB[i][6] == '¥':
            arregloB[i][6] = 'MXN'
            arregloB[i][7] = (float(arregloB[i][7]) * yenes)

        elif arregloB[i][6] == '$':
            arregloB[i][6] = 'MXN'
            arregloB[i][7] = (float(arregloB[i][7]) * dolares)

        elif arregloB[i][6] == '£':
            arregloB[i][6] = 'MXN'
            arregloB[i][7] = (float(arregloB[i][7]) * libras)

        else:
            pass

    return arregloB

# 6.- Imprimir el arreglo bidimensional.

def imprimirArregloB(arregloB):
    for i in range(0, len(arregloB)):
        for j in range(0, len(arregloB[0])):
            print(arregloB[i][j])

        print("\n ")


# 7.- Ordenar las cuentas.

def ordenarCuentas(arregloB):
    Elementos = []

    for i in range(0, len(arregloB)):
        existente = busqueda(Elementos, arregloB[i][0])
        if existente == False:
            Elementos.append(arregloB[i][0])
        else:
            pass
    return Elementos


# 8.- Generar las cuentas.

def generarCuentas(arreglo, arregloB):
    Elementos = []
    for i in range (0, len(arreglo)):
        DerivadoElementos = [arreglo[i],0,0]
        Elementos.append(DerivadoElementos)

    for i in range(0, len(Elementos)):
        for j in range(0, len(arregloB)):
            if Elementos[i][0] == arregloB[j][0]:
                Elementos[i][1] = arregloB[j][1] + ' '+arregloB[j][2]
            else:
                pass

    return Elementos

# 9.- Hacer Transacciones; reconocimiento de primera o segunda cuenta.

def transacciones(arregloB1, arregloB2):
    for i in range(0, len(arregloB1)):

        for j in range(0, len(arregloB2)):
            if arregloB2[j][0] == arregloB1[i][0]:
                arregloB1[i][2] = float(arregloB1[i][2]) - float(arregloB2[j][7])
            else:
                pass

        for k in range(0, len(arregloB2)):
            if arregloB2[k][3] == arregloB1[i][0]:
                arregloB1[i][2] = float(arregloB1[i][2]) + float(arregloB2[k][7])
            else:
                pass
    return arregloB1

# 10.- Hacer el diccionario de cuentas.

def generarDiccionario(arregloB):
    cuentas = {}
    for i in range(0, len(arregloB)):
        Cuentax = Cuenta(arregloB[i][0], arregloB[i][1],arregloB[i][2])
        cuentas[arregloB[i][0]] = Cuentax

    return cuentas

# 11.- Generar un archivo de análisis.

def generarArchivo(arregloB):
    archivo = open('analisis.txt', 'w')
    for i in range(0, len(arregloB)):
        archivo.write(arregloB[i][0] + ' ' + arregloB[i][1] + ' ' + str(arregloB[i][2]) + '\n')
    archivo.close



# 12.- Bloque para llamar funciones y métodos.

Transaccion = iArchivo('ResumenBancario.txt')
TransaccionEnPesosM = convertiraPesos(Transaccion)
NumeroDeCuentas = ordenarCuentas(TransaccionEnPesosM)
GeneracionCuentas = generarCuentas(NumeroDeCuentas,TransaccionEnPesosM)
GeneracionCuentas = transacciones(GeneracionCuentas,TransaccionEnPesosM)
Cuentas = generarDiccionario(GeneracionCuentas)
generarArchivo(GeneracionCuentas)

imprimirArregloB(GeneracionCuentas)
print(Cuentas)