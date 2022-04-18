from tkinter import *


window_1 = Tk()
window_1.title("Hola Mundo!")
window_1.geometry('500x400')

# Tamaño y fuente
lbl_1 = Label(window_1, text= "Hola Mundo", font=("Times", 30), foreground= 'pink', background= '#E03BBD')
lbl_1.grid(column=0, row =0)



#Botón
def click_1():
    lbl_1.configure(text = "Hola 1")

btn_1 = Button(window_1, text= "Click!", command= click_1)
btn_1.grid(column = 0, row=1, columnspan=2)


def click_2():
    lbl_1.configure(text = "Hola 2")

btn_2 = Button(window_1, text= "Click 2!", command=click_2)
btn_2.grid(column = 1, row=1)









window_1.mainloop()