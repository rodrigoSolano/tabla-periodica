from tkinter import *
import tkinter.font as tkFont
from tkinter import messagebox

from variables import *


class AgregarElemento(Button):

    def __init__(self, root, app, text, width, height, fila, columna, nombre_elemento):
        super().__init__(root, text=text, width=width, height=height)
        self.fila = fila
        self.columna = columna
        self.nombre_elemento = nombre_elemento
        self.app = app
        self.bind("<Button-1>", self.handleClick)

    def handleClick(self, event):

        nombre_elemento = self.app.currently_selected_item.properties[NOMBRE]
        self.ventana = Toplevel(self.app.frame, bg="white")
        self.ventana.title(f"Editar {nombre_elemento}")

        label_nombre = Label(self.ventana, text="Nombre: ",
                             bg="white", fg="black")
        label_nombre.grid(row=1, column=1, padx=5, pady=5)
        self.entry_nombre = Entry(self.ventana, width=15)
        self.entry_nombre.grid(row=1, column=2, padx=5, pady=5)

        label_numero_atomico = Label(
            self.ventana, text="Número atómico: ", bg="white", fg="black")
        label_numero_atomico.grid(row=2, column=1, padx=5, pady=5)
        self.entry_numero_atomico = Entry(self.ventana, width=15)
        self.entry_numero_atomico.grid(row=2, column=2, padx=5, pady=5)

        label_masa = Label(self.ventana, text="Masa: ", bg="white", fg="black")
        label_masa.grid(row=3, column=1, padx=5, pady=5)
        self.entry_masa = Entry(self.ventana, width=15)
        self.entry_masa.grid(row=3, column=2, padx=5, pady=5)

        label_simbolo = Label(
            self.ventana, text="Símbolo: ", bg="white", fg="black")
        label_simbolo.grid(row=4, column=1, padx=5, pady=5)
        self.entry_simbolo = Entry(self.ventana, width=15)
        self.entry_simbolo.grid(row=4, column=2, padx=5, pady=5)

        label_configuracion_electronica = Label(
            self.ventana, text="Configuración electrónica: ", bg="white", fg="black")
        label_configuracion_electronica.grid(row=5, column=1, padx=5, pady=5)
        self.entry_configuracion_electronica = Entry(self.ventana, width=15)
        self.entry_configuracion_electronica.grid(
            row=5, column=2, padx=5, pady=5)

        cancelar = Button(self.ventana, text="Cancelar", command=self.cancelar)
        cancelar.grid(row=6, column=1, pady=10)

        guardar = Button(self.ventana, text="Guardar",
                         command=self.guardar_datos)
        guardar.grid(row=6, column=2, pady=10)

        center(self.ventana)

    def guardar_datos(self):
        properties = {
            NOMBRE: self.entry_nombre.get(),
            SIMBOLO: self.entry_simbolo.get(),
            MASA: self.entry_masa.get(),
            CONF_ELECTRONICA: self.entry_configuracion_electronica.get(),
            N_ATOMICO: self.entry_numero_atomico.get(),
            TIPO: self.get_type_element(self.entry_nombre.get())
        }

        for e in self.app.elementos_faltantes:
            if e.fila == self.fila and e.columna == self.columna:
                if e.properties[NOMBRE] == self.entry_nombre.get():
                    self.ventana.destroy()
                    self.grid_remove()
                    self.app.agregar_elemento(properties,e.fila,e.columna)
                else:
                    messagebox.showerror(
                        message="El elemento no va en esa posición", title="Error")

    def cancelar(self):
        self.ventana.destroy()

    def get_type_element(self, nombre):
        if(nombre in OTROS_NO_METALES):
            return "otros_no_metales"
        if(nombre in METALES_ALCALINOS):
            return "metales_alcalinos"
        if(nombre in METALES_ALCALINOTERREOS):
            return "metales_alcalinoterreos"
        if(nombre in GASES_NOBLES):
            return "gases_nobles"
        if(nombre in METALOIDES):
            return "metaloides"
        if(nombre in HALOGENOS):
            return "halogenos"
        if(nombre.lower() in METALES_TRANSICION):
            return "metales_transicion"
        if(nombre in METALES_BLOQUE_P):
            return "metales_bloque_p"
        if(nombre in LANTANIDOS):
            return "lantanidos"
        if(nombre in ACTINIDOS):
            return "actinidos"


def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()
