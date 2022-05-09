import tkinter as tk
import tkinter.font as tkFont

class Alumno:
    def __init__(self,nombre, edad):
        self.Nombre = nombre
        self.Edad = edad

class App:
    def __init__(self, root):

        self. lista_alumnos = []
        self.last_selected_item = -1

        root.title("Formulario")

        width=500
        height=550
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_794=tk.Label(root, text = "Nombre:")
        GLabel_794.place(x=40,y=40,width=174,height=30)

        GLabel_408=tk.Label(root, text="Edad:")
        GLabel_408.place(x=40,y=110,width=174,height=30)

        self.txt_Nombre = tk.StringVar()
        self.txt_Nombre.set("")

        self.txt_Edad = tk.StringVar()
        self.txt_Edad.set("")



        self.GLineNombre=tk.Entry(root, borderwidth= "1px", textvariable= self.txt_Nombre)
        self.GLineNombre.place(x=250,y=40,width=148,height=34)

        self.GLineEdad=tk.Entry(root, borderwidth= "1px", textvariable= self.txt_Edad)
        self.GLineEdad.place(x=250,y=110,width=148,height=30)

        GButton_839=tk.Button(root, justify= "center", text="Agregar", command = self.CGButton_Agregar)
        GButton_839.place(x=50,y=180,width=142,height=30)


        GButton_130=tk.Button(root, justify= "center", text="Actualizar",command=self.CGButton_Actualizar)
        GButton_130.place(x=250,y=180,width=157,height=30)


        self.GListBox_Alumno=tk.Listbox(root, borderwidth= "1px")
        self.GListBox_Alumno.place(x=130,y=250,width=300,height=149)
        scrollbar = tk.Scrollbar(self.GListBox_Alumno)
        scrollbar.pack(side = tk.RIGHT, fill = tk.BOTH)
        self.GListBox_Alumno.config(yscrollcommand= scrollbar.set)
        scrollbar.config(command=self.GListBox_Alumno.yview)
        self.GListBox_Alumno.bind("<<ListboxSelect>>", self.itemSelect)


        GButtonEliminar=tk.Button(root, justify= "center", text="Eliminar",command=self.CGButton_Eliminar)
        GButtonEliminar.place(x=170,y=400,width=162,height=30)


        GButtonExportar=tk.Button(root, justify= "center", text="Exportar",command=self.CGButton_Exportar)
        GButtonExportar.place(x=170,y=460,width=162,height=30)

        GButtonImportar=tk.Button(root, justify= "center", text="Importar",command=self.CGButton_Importar)
        GButtonImportar.place(x=170,y=500,width=162,height=30)




    def itemSelect(self, event):
        index = self.GListBox_Alumno.curselection()
        if len(index) == 0:
            return

        index = index[0]
        self.last_selected_item = index
        alumno = self.lista_alumnos[index]

        self.txt_Nombre.set(alumno.Nombre)
        self.txt_Edad.set(alumno.Edad)


    def CGButton_Agregar(self):
        nombre = self.GLineNombre.get()
        edad = self.GLineEdad.get()

        if len(nombre) < 3 or not edad.isdigit():
            return

        alumno = Alumno(nombre, edad)
        self.lista_alumnos.append(alumno)
        self.GListBox_Alumno.insert(len(self.lista_alumnos)-1, nombre+", "+edad)
        self.txt_Nombre.set("")
        self.txt_Edad.set("")


        print(alumno)
        print(self.lista_alumnos)
        print(nombre +" , "+edad)


    def CGButton_Actualizar(self):
        if self.last_selected_item == -1:
            return

        index = self.last_selected_item

        nombre = self.GLineNombre.get()
        edad = self.GLineEdad.get()

        if len(nombre) < 3 or not edad.isdigit():
            return

        self.lista_alumnos[index].Nombre = nombre
        self.lista_alumnos[index].Nombre = edad
        self.GListBox_Alumno.delete(index)
        self.GListBox_Alumno.insert(index, nombre + ", " + edad)

        print("Actualizado")



    def CGButton_Eliminar(self):
        index = self.GListBox_Alumno.curselection()

        if len(index) == 0:
            return

        index = index[0]

        del self.lista_alumnos[index]
        self.GListBox_Alumno.delete(index)
        print(index)


    def CGButton_Exportar(self):
        file = open("Alumnos.txt", "w")
        for a in self.lista_alumnos:
            file.write(a.Nombre+ " | "+ a.Edad+ "\n")

        file.close()

    def CGButton_Importar(self):
        print()

