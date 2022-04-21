from tkinter import *

t = ""



def agregarNum(n):
    global t
    t = t + str(n)
    pantalla.set(t)




def limpiar():
    global t
    t = ""
    pantalla.set("")
    #pantalla.set(text= " ")

def presionar():
    global t

    try:

        total = str(eval(t))
        pantalla.set(str(total))
        t = ""

    except:
        pantalla.set("Error")
        t = ""


ventana = Tk()
ventana.title("Diseño_de_Calculadora")
ventana.geometry("220x280")


pantalla = StringVar()
mosPantalla = Entry(ventana, textvariable= pantalla)
mosPantalla.grid(columnspan= 4,ipadx= 25, ipady= 5)




b1 = Button(ventana, text= "  C", command= limpiar)
b1.grid(column=0, row= 2, padx=0, pady=0, ipadx=15, ipady=8)


bPot = Button(ventana, text= " ^",command= lambda: agregarNum('^'))
bPot.grid(column=1, row= 2, padx=0, pady=0, ipadx=15, ipady=8)

bPo = Button(ventana, text= " %", command= lambda: agregarNum('%'))
bPo.grid(column=2, row= 2, padx=0, pady=0, ipadx=15, ipady=8)

bD = Button(ventana, text= "/",command= lambda: agregarNum('/'))
bD.grid(column=3, row= 2, padx=0, pady=0, ipadx=15, ipady=8)



b5 = Button(ventana, text= "   7",  command= lambda: agregarNum(7))
b5.grid(column=0, row= 3, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('7')

b6 = Button(ventana, text= "   8",  command= lambda: agregarNum(8))
b6.grid(column=1, row= 3, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('8')

b7 = Button(ventana, text= "   9", command= lambda: agregarNum(9))
b7.grid(column=2, row= 3, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('9')

bM = Button(ventana, text= " *", command= lambda: agregarNum('*'))
bM.grid(column=3, row= 3, padx=0, pady=0, ipadx=15, ipady=8)


b9 = Button(ventana, text= "   4",  command= lambda: agregarNum(4))
b9.grid(column=0, row= 4, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('4')

b10 = Button(ventana, text= "   5",  command= lambda: agregarNum(5))
b10.grid(column=1, row= 4, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('5')

b11= Button(ventana, text= "   6", command= lambda: agregarNum(6))
b11.grid(column=2, row= 4, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('6')

bR= Button(ventana, text= " -", command= lambda: agregarNum('-'))
bR.grid(column=3, row= 4, padx=0, pady=0, ipadx=15, ipady=8)


b13 = Button(ventana, text= "   1",command= lambda:  agregarNum(1))
b13.grid(column=0, row= 5, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('1')


b14 = Button(ventana, text= "   2", command= lambda: agregarNum(2))
b14.grid(column=1, row= 5, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('2')

b15= Button(ventana, text= "   3",  command= lambda: agregarNum(3))
b15.grid(column=2, row= 5, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('3')

bS= Button(ventana, text= "+",command= lambda: agregarNum('+'))
bS.grid(column=3, row= 5, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('+')



b17 = Button(ventana, text= "   0", command= lambda: agregarNum(0))
b17.grid(column=0, row= 6, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('0')


bP= Button(ventana, text= "    .", command= lambda: agregarNum('.'))
bP.grid(column=2, row= 6, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('.')

bI= Button(ventana, text= "=", command =presionar)
bI.grid(column=3, row= 6, padx=0, pady=0, ipadx=15, ipady=8)
ventana.bind('=')




ventana.mainloop()