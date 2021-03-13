from tkinter import *

#importiere modul um zahlen als woerter darzustellen (auf englisch)
from num2words import num2words

fenster = Tk()

fenster.title("programm #1")
fenster.geometry('400x300')


def geklickt():
    global zahl
    zahl = zahl - 1
    
    print("es wurde geklickt!")
    anzeige.configure(text=zahl, font=("Elephant"))
    btn_1.configure(bg="red")
    
zahl = 0

def geklickt_2():
    global zahl
    zahl = zahl + 1
    
    anzeige.configure(text=zahl, font=("Elephant"))
    btn_2.configure(bg="green")

    if zahl % 5 == 0:
        # zahl wird jetzt eingefuegt in num2words
        a_text = "The number is " + num2words(zahl)
        #und der text im feld anzeige dargestellt
        anzeige.configure(text=a_text, font=("Elephant"))
        print(zahl)
        fenster.title(a_text)
        
btn_1 = Button(fenster, text="- 1", command=geklickt)
btn_1.grid(column=1, row=1, sticky=E , padx=10, pady=10)
    
btn_2 = Button(fenster, text="+ 1", command=geklickt_2)
btn_2.grid(column=3, row=1, padx=10, pady=10)

anzeige = Label(fenster, text="Anzeigentext134rwwr")
anzeige.grid(column=1, row=2, padx=10, pady=10)

anzeige_2 = Label(fenster, text="Hallo wie gehts?")
anzeige_2.grid(column=1, row=5, padx=10, pady=10)

# hier noch ein eingabefeld
eingabe = Entry(fenster)
eingabe.grid(column=1, row=6, padx=10, pady=10)


