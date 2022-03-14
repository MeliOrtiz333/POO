import threading as th
import time


up_count = 0
down_count = 100


hilos = {
    "hilo1": None,
    "hilo2": None
}


#r = '' (Para un menu con S y salir


def hilo1_start():
    global up_count, hilos
    up_count += 1
    if up_count < 100:
        hilos["hilo1"] = th.Timer(5, hilo1_start)
        hilos["hilo1"].start()


def hilo2_start():
    global down_count, hilos
    down_count -= 1
    if down_count > 0:
        hilos["hilo2"] = th.Timer(7, hilo2_start)
        hilos["hilo2"].start()



def detener_hilos():
    global hilos
    hilos["hilos1"].cancel()
    hilos["hilos2"].cancel()

hilo1_start()
hilo2_start()


stop_count = 0
while stop_count < 50:
    print("up: " + str(up_count) + "- down:" + str(down_count))
    time.sleep(2)
    stop_count += 1

detener_hilos()

