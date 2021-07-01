import csv
SIZE_BLOCK = 3
PADX = 2
PADY = 1
# Propiedades de un elemento quimico
N_ATOMICO = "n_atomico"
SIMBOLO = "simbolo"
NOMBRE = "nombre"
MASA = "masa"
PERIODO = "periodo"
GRUPO = "grupo"
ESTRUCTURA = "estructura"
CONF_ELECTRONICA = "conf_electronica"
DENSIDAD = "densidad"
TIPO = "tipo"
COORDS = "coordenandas"

def crearElementos():
    lista_elementos = list()
    with open('data.csv', newline='') as f:
        reader = csv.reader(f)
        elementos = list(reader)
    keys = elementos.pop(0)
    for e in elementos:
        element = dict()
        i = 0
        for key in keys:
            if key == N_ATOMICO:
                element[key] = int(e[i])
            else:
                element[key] = e[i]
            i += 1
        lista_elementos.append(element)
    return lista_elementos


TIPOS_ELEMENTOS = [
    "otros_no_metales",
    "metales_alcalinos",
    "metales_alcalinoterreos",
    "gases_nobles",
    "metaloides",
    "halogenos",
    "metales_transicion",
    "metales_bloque_p",
    "lantanidos",
    "actinidos"
]


COLORES_TIPOS_ELEMENTOS = {
    "otros_no_metales": "#F58021",
    "metales_alcalinos": "#002A4E",
    "metales_alcalinoterreos": "#FDBA12",
    "gases_nobles": "#006A36",
    "metaloides": "#ED1944",
    "halogenos": "#A2B427",
    "metales_transicion": "#0088CE",
    "metales_bloque_p": "#781E77",
    "lantanidos": "#CBD48E",
    "actinidos": "#67A484"
}

OTROS_NO_METALES = [
    "Hidrogeno",
    "Carbono",
    "Nitrogeno",
    "Oxigeno",
    "Fosforo",
    "Azufre",
    "Selenio"
]

METALES_ALCALINOS = [
    "Litio",
    "Sodio",
    "Potasio",
    "Rubidio",
    "Cesio",
    "Francio"
]

METALES_ALCALINOTERREOS = [
    "Berilio",
    "Magnesio",
    "Calcio",
    "Estroncio",
    "Bario",
    "Radio"
]

GASES_NOBLES = [
    "Helio",
    "Neon",
    "Argon",
    "Kripton",
    "Xenon",
    "Radon",
    "Oganeson"
]

METALOIDES = [
    "Boro",
    "Silicio",
    "Germanio",
    "Arsenico",
    "Antimonio",
    "Telurio",
    "Polonio"
]

HALOGENOS = [
    "Fluor",
    "Cloro",
    "Bromo",
    "Yodo",
    "Astato",
    "Tenesino"
]

METALES_TRANSICION = [
    "titanio",
    "vanadio",
    "cromo",
    "manganeso",
    "hierro",
    "cobalto",
    "niquel",
    "cobre",
    "circonio",
    "niobio",
    "molibdeno",
    "tecnecio",
    "rutenio",
    "rodio",
    "paladio",
    "plata",
    "hafnio",
    "tantalio",
    "wolframio",
    "renio",
    "osmio",
    "iridio",
    "platino",
    "oro",
    "escandio",
    "itrio",
    "zinc",
    "cadmio",
    "mercurio",
    "rutherfordio",
    "dubnio",
    "seaborgio",
    "bohrio",
    "hassio",
    "meitnerio",
    "darmstadtio",
    "roentgenio",
    "copernicio"]

METALES_BLOQUE_P = [
    "Aluminio",
    "Galio",
    "Indio",
    "Estaño",
    "Talio",
    "Plomo",
    "Bismuto",
    "Nihonio",
    "Flerovio",
    "Moscovio",
    "Livermorio"
]

LANTANIDOS = [
    "Lantano",
    "Cerio",
    "Praseodimio",
    "Neodimio",
    "Prometio",
    "Samario",
    "Europio",
    "Gadolin",
    "Terbio",
    "Disprosio",
    "Holmio",
    "Erbio",
    "Tulio",
    "Iterbio",
    "Lutecio",
]

ACTINIDOS = [
    "Actinio",
    "Torio",
    "Protactinio",
    "Uranio",
    "Neptunio",
    "Plutonio",
    "Americio",
    "Curio",
    "Berkelio",
    "Californio",
    "Einstenio",
    "Fermio",
    "Mendelevio",
    "Nobelio",
    "Laurencio",
]
