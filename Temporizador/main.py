import threading as th


i = 0
j = int(input("Contar hasta:   "))

def contar():
    global i,j
    print("> ",i)
    i += 1
    hilo = th.Timer(3.0, contar)
    hilo.start()
    if i > j:
        hilo.cancel()

contar()
