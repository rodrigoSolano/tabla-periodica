from tkinter import *
import tkinter.font as tkFont

from variables import *
from Clasificacion import ClasificacionElemento
from Element import Element
from SelectedItem import SelectecItem
from AgregarElemento import AgregarElemento

class PeriodicTable():

    def __init__(self, window):
        ####################################################################################
        self.window = window
        self.window.configure(bg="#fff")
        self.window.title("Tabla periódica de los elementos")

        ####################################################################################
        self.titulo = Label(
            self.window,
            text="TABLA PERIÓDICA DE LOS ELEMENTOS", fg="#002A4E",
            bg="white",
            font=tkFont.Font(family='Helvetica', size=18, weight='bold')
        )
        self.titulo.grid(row=0, column=0, padx=PADX, pady=PADY*10)

        ####################################################################################
        self.frame = Frame(self.window, bg="#fff")
        self.frame.grid(row=2, column=0, padx=20, pady=PADY)

        ####################################################################################
        self.elementos_faltantes = list()
        self.elements = list()
        self.selected_type_element = None

        ####################################################################################
        self.create_row_and_column_labels()
        self.agregar_elementos()

        ####################################################################################
        self.currently_selected_item = SelectecItem(
            root=self.frame,
            bg=self.elements[0].bg,
            fg=self.elements[0].fg,
            properties=self.elements[0].properties
        )
        self.currently_selected_item.grid(
            row=1,
            column=3,
            rowspan=3,
            columnspan=3,
            pady=PADY,
            padx=PADX
        )

        # ####################################################################################
        self.clasificacion_elementos = Frame(self.frame, bg="white")
        self.clasificacion_elementos.grid(
            row=1, column=6, columnspan=7, rowspan=3)

        # ####################################################################################

        fila = 0
        columna = 0
        for elemento in TIPOS_ELEMENTOS:
            tipo_elemento = ClasificacionElemento(
                self.clasificacion_elementos,
                bg=COLORES_TIPOS_ELEMENTOS[elemento],
                nombre=elemento,
                app=self
            )
            tipo_elemento.grid(row=fila, column=columna, pady=PADY, padx=PADX)
            fila += 1
            if(fila == 5):
                fila = 0
                columna += 1

        # ####################################################################################

        self.eliminar = Button(
            self.frame,
            text="Eliminar",
            fg="black",
            bg="white",
            anchor="e",
            command=self.eliminar_elemento
        )
        self.eliminar.grid(column=1, row=13,columnspan=2,pady=PADY*10)

        self.editar = Button(
            self.frame,
            text="Editar",
            fg="black",
            bg="white",
            anchor="e",
            command=self.editar_elemento
        )
        self.editar.grid(column=3, row=13,columnspan=2,pady=PADY*10)
        
        self.label_info = Label(
            self.frame,
            text="Elemento Seleccionado: Hidrogeno",
            fg="black",
            bg="white",
            anchor="e"
        )
        self.label_info.grid(column=5, row=13, columnspan=7,pady=PADY*10)
      
    def editar_elemento(self):
        nombre_elemento = self.currently_selected_item.properties[NOMBRE]
        self.ventana = Toplevel(self.window, bg="white")
        self.ventana.title(f"Editar {nombre_elemento}")

        label_nombre = Label(self.ventana, text="Nombre: ",
                             bg="white", fg="black")
        label_nombre.grid(row=1, column=1, padx=5, pady=5)
        self.entry_nombre = Entry(self.ventana, width=15)
        self.entry_nombre.insert(0,self.currently_selected_item.properties[NOMBRE])
        self.entry_nombre.grid(row=1, column=2, padx=5, pady=5)

        label_numero_atomico = Label(
            self.ventana, text="Numero atomico: ", bg="white", fg="black")
        label_numero_atomico.grid(row=2, column=1, padx=5, pady=5)
        self.entry_numero_atomico = Entry(self.ventana, width=15)
        self.entry_numero_atomico.insert(0,self.currently_selected_item.properties[N_ATOMICO])
        self.entry_numero_atomico.grid(row=2, column=2, padx=5, pady=5)

        label_masa = Label(self.ventana, text="Masa: ", bg="white", fg="black")
        label_masa.grid(row=3, column=1, padx=5, pady=5)
        self.entry_masa = Entry(self.ventana, width=15)
        self.entry_masa.insert(0,self.currently_selected_item.properties[MASA])
        self.entry_masa.grid(row=3, column=2, padx=5, pady=5)

        label_simbolo = Label(
            self.ventana, text="Simbolo: ", bg="white", fg="black")
        label_simbolo.grid(row=4, column=1, padx=5, pady=5)
        self.entry_simbolo = Entry(self.ventana, width=15)
        self.entry_simbolo.insert(0,self.currently_selected_item.properties[SIMBOLO])
        self.entry_simbolo.grid(row=4, column=2, padx=5, pady=5)

        label_configuracion_electronica = Label(
            self.ventana, text="Configuracion electronica: ", bg="white", fg="black")
        label_configuracion_electronica.grid(row=5, column=1, padx=5, pady=5)
        self.entry_configuracion_electronica = Entry(self.ventana, width=15)
        self.entry_configuracion_electronica.insert(0,self.currently_selected_item.properties[CONF_ELECTRONICA])
        self.entry_configuracion_electronica.grid(
            row=5, column=2, padx=5, pady=5)

        cancelar = Button(self.ventana, text="Cancelar", command=(lambda:self.ventana.destroy()))
        cancelar.grid(row=6, column=1, pady=10)

        guardar = Button(self.ventana, text="Guardar",
                         command=self.guardar_datos)
        guardar.grid(row=6, column=2, pady=10)

        self.center(self.ventana)

    def guardar_datos(self):
        properties = {
            NOMBRE: self.entry_nombre.get(),
            SIMBOLO: self.entry_simbolo.get(),
            MASA: self.entry_masa.get(),
            CONF_ELECTRONICA: self.entry_configuracion_electronica.get(),
            N_ATOMICO: self.entry_numero_atomico.get(),
            TIPO: self.currently_selected_item.properties[TIPO]
        }
        for e in self.elements:
            if e.properties == self.currently_selected_item.properties:
                e.grid_forget()
                fila = self.currently_selected_item.properties["fila"]
                columna = self.currently_selected_item.properties["columna"]
                elemento = self.agregar_elemento(properties,fila,columna)
                self.elements.remove(e)
                self.elements.append(elemento)
                self.seleccionar_elemento(elemento.properties,elemento.bg,elemento.fg)
        self.ventana.destroy()

    def eliminar_elemento(self):
        for elemento in self.elements:
            if elemento.properties[NOMBRE] == self.currently_selected_item.properties[NOMBRE]:

                self.elementos_faltantes.append(elemento)

                fila = elemento.coords[0]
                columna = elemento.coords[1]
                agregar_nuevo_elemento = AgregarElemento(
                    self.frame,
                    text="+",
                    width=SIZE_BLOCK,
                    height=SIZE_BLOCK,
                    nombre_elemento=elemento.properties[NOMBRE],
                    fila=fila,
                    columna=columna,
                    app=self)

                agregar_nuevo_elemento.grid(row=elemento.x, column=elemento.y)

                elemento.grid_forget()

    def agregar_elemento(self, properties, fila, columna):
        properties["fila"] = fila
        properties["columna"] = columna
        elemento = Element(
            root=self.frame,
            app=self,
            bg=self.get_bg(properties),
            command=self.seleccionar_elemento,
            coords=(fila, columna),
            properties=properties
        )
        elemento.grid(row=fila, column=columna)
        return elemento

    def create_row_and_column_labels(self):
        # Labels horizontales
        for i in range(1, 19):
            label = Label(self.frame, text=i, bg="white", fg="black", width=3)
            label.grid(row=0, column=i, pady=PADY, padx=PADX)

        # Labels verticales
        for i in range(1, 8):
            label = Label(self.frame, text=i, bg="white", fg="black", width=3)
            label.grid(row=i, column=0, padx=PADX, pady=PADY)

    def agregar_elementos(self):
        elementos = crearElementos()
        for elemento in elementos:
            element = Element(
                root=self.frame,
                app=self,
                bg=self.get_bg(elemento),
                command=self.seleccionar_elemento,
                coords=(elemento["fila"], int(elemento["columna"])),
                properties=elemento
            )
            element.grid(
                row=elemento["fila"],
                column=elemento["columna"],
                pady=PADY,
                padx=PADX
            )
            self.elements.append(element)

        boton_lantanidos = Button(self.frame,
                                  text="La-Lu",
                                  height=SIZE_BLOCK,
                                  width=SIZE_BLOCK,
                                  background="#CBD48E",
                                  activebackground="#c0d7f0",
                                  borderwidth=0,
                                  font=tkFont.Font(family='Helvetica', size=11, weight='bold'))
        boton_lantanidos.grid(row=6, column=3, pady=PADY, padx=PADX)

        boton_actínidos = Button(self.frame,
                                 text="Ac-Lr",
                                 height=SIZE_BLOCK,
                                 width=SIZE_BLOCK,
                                 background="#67A484",
                                 activebackground="#c0d7f0",
                                 borderwidth=0,
                                 font=tkFont.Font(family='Helvetica', size=11, weight='bold'))
        boton_actínidos.grid(row=7, column=3, pady=PADY, padx=PADX)

        label_info = Label(self.frame,
                           text="Para los elementos isotopos estables, el numero de masa del isotopo con la vida media mas larga esta en parentesis",
                           height=2,
                           bg="#fff",
                           fg="#000")

        label_info.grid(row=8, column=4, columnspan=14, rowspan=2, sticky=W)

    def get_bg(self, elemento):
        return COLORES_TIPOS_ELEMENTOS[elemento[TIPO]]

    def seleccionar_elemento(self, properties, bg, fg):
        self.label_info.configure(
            text="Elemento Seleccionado: "+properties[NOMBRE])
        self.currently_selected_item.change_element(
            properties=properties,
            bg=bg,
            fg=fg)
        self.window.update_idletasks()
        self.frame.update_idletasks()

    def filtrar_elementos(self, type_element):

        if(self.selected_type_element != None):
            if(self.selected_type_element == type_element):
                self.selected_type_element = None
                for e in self.elements:
                    e.active()
            else:
                self.selected_type_element = type_element
                for e in self.elements:
                    e.active()
                elementos = list(
                    filter(lambda element: element.properties[TIPO] == type_element, self.elements))
                for e in self.elements:
                    if e not in elementos:
                        e.disable()
        else:
            self.selected_type_element = type_element
            elementos = list(
                filter(lambda element: element.properties[TIPO] == type_element, self.elements))
            for e in self.elements:
                if e not in elementos:
                    e.disable()

    def center(self,win):
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

def main():
    window = Tk()
    application = PeriodicTable(window)
    window.mainloop()

if __name__ == '__main__':
    main()
