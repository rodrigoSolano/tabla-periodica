from variables import *
from tkinter import *
import tkinter.font as tkFont
from colorsys import rgb_to_hls, hls_to_rgb
import re

class Element(Button):
    def __init__(self,root,app,bg,command,coords,properties):
        super().__init__(root)
        self.root = root
        self.app = app
        self.bg = bg
        self.command = command
        self.coords = coords
        self.x = coords[0]
        self.y = coords[1]
        self.fila = coords[0]
        self.columna = coords[1]
        self.state = ACTIVE
        self.properties = properties
        self.font_style = tkFont.Font(family='Helvetica', size=11, weight='bold')
        self.fg = self.getForeground(self.properties[TIPO])
       

        super().__init__(root,
                         text=self.properties[SIMBOLO], 
                         height=SIZE_BLOCK, 
                         width=SIZE_BLOCK,
                         font=self.font_style,
                         activebackground=self.getActiveColor(self.bg),
                         background=bg,
                         borderwidth=0,
                         foreground=self.fg,
                         command=None,
                         )

        self.bind("<Button-1>", self.handleClick)
        
    def getForeground(self,type):
        if(type == "actinidos" or type == "lantanidos" or type == "otros_no_metales" or type == "metales_alcalinoterreos" or type == "halogenos" ):
            return "#000"
        return  "#fff"
        
    def getActiveColor(self, bg):
        rbg_code = self.hex_to_rgb(bg)
        rgb_lighten_color = self.lighten_color(
            rbg_code[0], rbg_code[1], rbg_code[2])
        return "#" + ('%02x%02x%02x' % rgb_lighten_color)

    def hex_to_rgb(self, hx, hsl=False):
        if re.compile(r'#[a-fA-F0-9]{3}(?:[a-fA-F0-9]{3})?$').match(hx):
            div = 255.0 if hsl else 0
            if len(hx) <= 4:
                return tuple(int(hx[i]*2, 16) / div if div else
                             int(hx[i]*2, 16) for i in (1, 2, 3))
            return tuple(int(hx[i:i+2], 16) / div if div else
                         int(hx[i:i+2], 16) for i in (1, 3, 5))
        raise ValueError(f'"{hx}" is not a valid HEX code.')

    def lighten_color(self, r, g, b, factor=0.2):
        return self.adjust_color_lightness(r, g, b, 1 + factor)

    def adjust_color_lightness(self, r, g, b, factor):
        h, l, s = rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
        l = max(min(l * factor, 1.0), 0.0)
        r, g, b = hls_to_rgb(h, l, s)
        return int(r * 255), int(g * 255), int(b * 255)

    def handleClick(self, event):
        if(self.state == DISABLED):
            return
        self.command(
            properties=self.properties,
            fg=self.fg,
            bg=self.bg)
    
    def disable(self):
        self.state = DISABLED
        self["state"] = DISABLED
        self["bg"] = "#FFF"
        self["fg"] = "#000"

    def active(self):
        self.state = NORMAL
        self["state"] = NORMAL
        self["bg"] = self.bg
        self["fg"] = self.fg
   