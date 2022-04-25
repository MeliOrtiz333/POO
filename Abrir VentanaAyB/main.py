import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter.ttk import *



def openNewWindowA():


    newWindow = Toplevel(root)

    newWindow.title("Ventana A")


    newWindow.geometry("200x200")


    Label(newWindow,
          text ="Esta es la Ventana A").pack()








def openNewWindowB():


    newWindow = Toplevel(root)


    newWindow.title("Ventana B")


    newWindow.geometry("200x200")


    Label(newWindow,
          text ="Esta es la Ventana B").pack()











class App:
    def __init__(self, root):
        #setting title
        root.title("Ventanas")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_560=tk.Button(root)
        GButton_560["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=18)
        GButton_560["font"] = ft
        GButton_560["fg"] = "#000000"
        GButton_560["justify"] = "center"
        GButton_560["text"] = "Ventana A"
        GButton_560.place(x=160,y=210,width=120,height=90)
        GButton_560["command"] = self.GButton_560_command

        GButton_230=tk.Button(root)
        GButton_230["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=18)
        GButton_230["font"] = ft
        GButton_230["fg"] = "#000000"
        GButton_230["justify"] = "center"
        GButton_230["text"] = "Ventana B"
        GButton_230.place(x=160,y=350,width=120,height=90)
        GButton_230["command"] = self.GButton_230_command



    def GButton_560_command(self):
        print("Esta es la ventana A")
        openNewWindowA()


    def GButton_230_command(self):
        print("Esta es la ventana B")
        openNewWindowB()




if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
