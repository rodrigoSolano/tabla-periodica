from tkinter import *
import tkinter.font as tkFont
from variables import PADX, PADY


class ClasificacionElemento(Frame):
    def __init__(self, root, bg, nombre, app):
        super().__init__(root, bg="white")
        self.nombre = nombre
        self.app = app

        font = tkFont.Font(family='Helvetica', size=10, weight='normal')

        nombre = " ".join(nombre.capitalize().split("_"))

        color = Label(self, text="", bg=bg, width=2)
        color.grid(row=0, column=1)


        sep2 = Label(self,text="", bg="white",fg="white")
        sep2.grid(row=0, column=2)

        label_nombre = Label(
            self,
            text=nombre,
            width=22,
            bg="#fff",
            fg="#000",
            anchor="w",
            font=font
        )
        label_nombre.grid(row=0, column=3, pady=PADY*4, padx=0)

        
        self.bind("<Button-1>", self.handleClick)
        label_nombre.bind("<Button-1>", self.handleClick)
        color.bind("<Button-1>", self.handleClick)

    def handleClick(self, event):
        self.app.filtrar_elementos(self.nombre)
