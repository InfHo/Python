# importiere tkinter modul
from tkinter import *

# erstelle fenster
fenster = Tk()

# stelle fenstergroesse ein
fenster.geometry('400x300')

# erstelle knop und nennen  ihn "btn"
btn = Button(fenster, text="Klick")

# positionierung mit grid, column = spalte, row = zeile
btn.grid(column=1, row=1)
