from tkinter import *
import tkinter.font as tkFont
from variables import *

width = 8
height = 2
bg = "#F58021"
fg = "#000"


class SelectecItem(Frame):
    def __init__(self, root, bg, fg, properties):
        super().__init__(root, bg=bg)
        self.root = root
        self.fg = fg
        self.bg = bg
        self.properties = properties
        self.font_style = tkFont.Font(
            family='Helvetica',
            size=12,
            weight='bold'
        )

        # Numero atomico
        self.label_numero_atomico = Label(
            self,
            text=self.properties[N_ATOMICO],
            bg=bg,
            fg=fg,
            font=self.font_style,
            anchor="w"
        )
        self.label_numero_atomico.grid(
            row=0,
            column=0,
            columnspan=9,
            padx=PADX,
            pady=PADY*7
        )

        # Masa
        self.label_masa = Label(
            self,
            text=self.properties[MASA],
            bg=bg,
            fg=fg,
            font=self.font_style)
        self.label_masa.grid(
            row=0,
            column=8,
            columnspan=9,
            padx=PADX,
            pady=PADY*4
        )

        # Simbolo
        self.label_simbolo = Label(
            self,
            text=self.properties[SIMBOLO],
            bg=bg,
            fg=fg,
            font=tkFont.Font(
                family='Helvetica', size=20, weight='bold'))
        self.label_simbolo.grid(
            row=1,
            column=0,
            columnspan=18,
            padx=PADX,
            pady=PADY*4
        )

        # Nombre
        self.label_nombre = Label(
            self,
            text=self.properties[NOMBRE],
            width=16,
            height=1,
            bg=bg,
            fg=fg,
            font=self.font_style)
        self.label_nombre.grid(
            row=2,
            column=0,
            columnspan=18,
            padx=PADX,
            pady=PADY*4
        )

        # conficuracion electronica
        self.label_conf_electronica = Label(
            self,
            text=self.properties[CONF_ELECTRONICA],
            bg=bg,
            fg=fg,
            font=tkFont.Font(family='Helvetica', size=9, weight='bold'))
        self.label_conf_electronica.grid(
            row=3,
            column=0,
            columnspan=18,
            padx=PADX,
            pady=PADY*7
        )

    def change_element(self, bg, fg, properties):
        self.properties = properties
        self.label_numero_atomico["text"] = properties[N_ATOMICO]
        self.label_numero_atomico["bg"] = bg
        self.label_numero_atomico["fg"] = fg

        self.label_masa["text"] = properties[MASA]
        self.label_masa["bg"] = bg
        self.label_masa["fg"] = fg

        self.label_simbolo["text"] = properties[SIMBOLO]
        self.label_simbolo["bg"] = bg
        self.label_simbolo["fg"] = fg

        self.label_nombre["text"] = properties[NOMBRE]
        self.label_nombre["bg"] = bg
        self.label_nombre["fg"] = fg

        self.label_conf_electronica["text"] = properties[CONF_ELECTRONICA]
        self.label_conf_electronica["bg"] = bg
        self.label_conf_electronica["fg"] = fg

        self.configure(bg=bg)
