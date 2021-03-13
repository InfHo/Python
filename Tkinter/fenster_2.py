from tkinter import *

fenster = Tk()

fenster.geometry('400x300')

# erstelle funktion 
def geklickt():
    print("es wurde geklickt!")
    anzeige.configure(text="Hallo")

# fuege die funktion geklickt hier ein und veraendere groesse von knopf
btn = Button(fenster, text="Klick", height=10, width=20, command=geklickt)
btn.grid(column=1, row=1)

# erstelle anzeige und positioniere sie mit grid
anzeige = Label(fenster, text="Anzeigentext134")
anzeige.grid(column=1, row=2)
