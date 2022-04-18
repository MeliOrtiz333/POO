from tkinter import *

ventana = Tk()
ventana.title("Diseño_de_Calculadora")
ventana.geometry("250x400")

titulo = Label(ventana, text = "Calculadora", font=("Times",13),fg= 'blue')
titulo.grid(column= 0, row=0)


pantalla = Button(ventana, text = "                      0")
pantalla.grid(column=0, row= 1, padx=10, pady= 10, ipadx=70, ipady=10,columnspan= 4)

b1 = Button(ventana, text= "C")
b1.grid(column=0, row= 2, padx=0, pady=0, ipadx=15, ipady=8)

b2 = Button(ventana, text= "+/-")
b2.grid(column=1, row= 2, padx=0, pady=0, ipadx=15, ipady=8)

b3 = Button(ventana, text= "%")
b3.grid(column=2, row= 2, padx=0, pady=0, ipadx=15, ipady=8)

b4 = Button(ventana, text= "°/.")
b4.grid(column=3, row= 2, padx=0, pady=0, ipadx=15, ipady=8)



b5 = Button(ventana, text= "7")
b5.grid(column=0, row= 3, padx=0, pady=0, ipadx=15, ipady=8)

b6 = Button(ventana, text= "8")
b6.grid(column=1, row= 3, padx=0, pady=0, ipadx=15, ipady=8)

b7 = Button(ventana, text= "9")
b7.grid(column=2, row= 3, padx=0, pady=0, ipadx=15, ipady=8)

b8 = Button(ventana, text= "x")
b8.grid(column=3, row= 3, padx=0, pady=0, ipadx=15, ipady=8)


b9 = Button(ventana, text= "4")
b9.grid(column=0, row= 4, padx=0, pady=0, ipadx=15, ipady=8)

b10 = Button(ventana, text= "5")
b10.grid(column=1, row= 4, padx=0, pady=0, ipadx=15, ipady=8)

b11= Button(ventana, text= "6")
b11.grid(column=2, row= 4, padx=0, pady=0, ipadx=15, ipady=8)

b12= Button(ventana, text= "-")
b12.grid(column=3, row= 4, padx=0, pady=0, ipadx=15, ipady=8)


b13 = Button(ventana, text= "1")
b13.grid(column=0, row= 5, padx=0, pady=0, ipadx=15, ipady=8)

b14 = Button(ventana, text= "2")
b14.grid(column=1, row= 5, padx=0, pady=0, ipadx=15, ipady=8)

b15= Button(ventana, text= "3")
b15.grid(column=2, row= 5, padx=0, pady=0, ipadx=15, ipady=8)

b16= Button(ventana, text= "+")
b16.grid(column=3, row= 5, padx=0, pady=0, ipadx=15, ipady=8)


b17 = Button(ventana, text= "0")
b17.grid(column=0, row= 6, padx=0, pady=0, ipadx=15, ipady=8)

b18 = Button(ventana, text= "(  )")
b18.grid(column=1, row= 6, padx=0, pady=0, ipadx=15, ipady=8)

b19= Button(ventana, text= ".")
b19.grid(column=2, row= 6, padx=0, pady=0, ipadx=15, ipady=8)

b20= Button(ventana, text= "=")
b20.grid(column=3, row= 6, padx=0, pady=0, ipadx=15, ipady=8)




ventana.mainloop()