import tkinter as tk
import tkinter.font as tkFont

list=["","","",""]
class App:
    def __init__(self, root):
        root.title("¿Qué número es?")
        width=530
        height=550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GLineEdit_975=tk.Entry(root)
        self.GLineEdit_975["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_975["font"] = ft
        self.GLineEdit_975["fg"] = "#333333"
        self.GLineEdit_975["justify"] = "center"
        self.GLineEdit_975["text"] = "Entry"
        self.GLineEdit_975.place(x=150,y=40,width=218,height=42)

        GButton_696=tk.Button(root)
        GButton_696["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_696["font"] = ft
        GButton_696["fg"] = "#000000"
        GButton_696["justify"] = "center"
        GButton_696["text"] = "-"
        GButton_696.place(x=50,y=40,width=66,height=46)
        GButton_696["command"] = self.GButton_696_command

        GButton_430=tk.Button(root)
        GButton_430["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_430["font"] = ft
        GButton_430["fg"] = "#000000"
        GButton_430["justify"] = "center"
        GButton_430["text"] = "+"
        GButton_430.place(x=400,y=40,width=71,height=48)
        GButton_430["command"] = self.GButton_430_command

        self.GLabel_706=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_706["font"] = ft
        self.GLabel_706["fg"] = "#333333"
        self.GLabel_706["justify"] = "center"
        self.GLabel_706["text"] = "El número:"
        self.GLabel_706.place(x=130,y=160,width=258,height=30)

        self.GLabel_893=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_893["font"] = ft
        self.GLabel_893["fg"] = "#333333"
        self.GLabel_893["justify"] = "center"
        self.GLabel_893["text"] = "Par/Impar"
        self.GLabel_893.place(x=140,y=220,width=234,height=30)

        self.GLabel_392=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_392["font"] = ft
        self.GLabel_392["fg"] = "#333333"
        self.GLabel_392["justify"] = "center"
        self.GLabel_392["text"] = "Biciesto"
        self.GLabel_392.place(x=120,y=280,width=274,height=30)

        self.GLabel_911=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_911["font"] = ft
        self.GLabel_911["fg"] = "#333333"
        self.GLabel_911["justify"] = "center"
        self.GLabel_911["text"] = "Multiplo de 3/5/7"
        self.GLabel_911.place(x=130,y=340,width=250,height=34)

        self.GLabel_912=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_912["font"] = ft
        self.GLabel_912["fg"] = "#333333"
        self.GLabel_912["justify"] = "center"
        self.GLabel_912["text"] = "No/Primo"
        self.GLabel_912.place(x=130,y=380,width=250,height=34)

    def GButton_696_command(self):
        num=int(self.GLineEdit_975.get())
        self.GLineEdit_975.delete(0,tk.END)
        numnuevo=num-1
        if numnuevo>=0:
            self.GLineEdit_975.insert(0,str(numnuevo))
            self.validar(numnuevo)
        else:
            self.GLineEdit_975.insert(0, str(num))
            self.validar(num)



    def GButton_430_command(self):
        num = int(self.GLineEdit_975.get())
        self.GLineEdit_975.delete(0,tk.END)
        numnuevo=num + 1
        self.GLineEdit_975.insert(0, str(numnuevo))
        self.validar(numnuevo)

    def validar(self, num):
        #Condicional pares
        if num%2==0:
            list[0]="Par"
        else:
            list[0]="Impar"

        #Condicional Biciesto
        if num%400==0:
            list[1] = "Biciesto"
        elif num%100!=0 and num%4==0:
            list[1] = "Biciesto"
        else:
            list[1] = "No Biciesto"

        #Condicional multiplos
        if num%3==0 and num%5==0 and num%7==0:
            list[2] = "Multiplo de 3 5 y 7"
        elif num%3==0 and num%5==0 and num%7!=0:
            list[2] = "Multiplo de 3 y 5"
        elif num%3==0 and num%5!=0 and num%7==0:
            list[2] = "Multiplo de 3 y 7"
        elif num%3!=0 and num%5==0 and num%7==0:
            list[2] = "Multiplo de 5 y 7"
        elif num%3==0 and num%5!=0 and num%7!=0:
            list[2] = "Multiplo de 3"
        elif num%3!=0 and num%5==0 and num%7!=0:
            list[2] = "Multiplo de 5"
        elif num%3!=0 and num%5!=0 and num%7==0:
            list[2] = "Multiplo de 7"
        else:
            list[2] = "No es multiplo de 3 ni 5 ni 7"

        #Condicional Primos
        for i in range (2,num+1):
            for x in range (1,i+1):
                primo=True
                res=i%x
                if res==0 and x!=1 and x!=i:
                    primo=False
                    break
            if primo==True:
                list[3]="Primo"
                num+=1
            else:
                list[3]="No primo"

        self.GLabel_893.config(text=list[0])
        self.GLabel_392.config(text=list[1])
        self.GLabel_911.config(text=list[2])
        self.GLabel_912.config(text=list[3])


        print(list)

        pass



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
