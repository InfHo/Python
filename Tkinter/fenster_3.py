from tkinter import *

fenster = Tk()

fenster.geometry('400x300')

def geklickt():
	# erstelle variable zahl und mache sie global, dh sie 
	# existiert jetzt auch ausserhalb der funtion
    global zahl
    zahl = zahl - 1
    
    print("es wurde geklickt!")
    anzeige.configure(text=zahl, font=("Elephant"))
    btn_1.configure(bg="red")
    
zahl = 0

fuenfer_reihe = ["fünf","zehn","fünfzehn","zwanzig"]

def geklickt_2():
    global zahl
    zahl = zahl + 1
    
    anzeige.configure(text=zahl, font=("Elephant"))
    btn_2.configure(bg="green")

    # immer wenn zahl aus 5er reihe...
    if zahl % 5 == 0:
    	# ... fuehre folgende Befehle aus
        anzeige.configure(text="Die Zahl ist jetzt Fünf", font=("Elephant"))
        print(zahl)
        
btn_1 = Button(fenster, text="- 1", command=geklickt)
btn_1.grid(column=1, row=1, sticky=E , padx=10, pady=10)
    
btn_2 = Button(fenster, text="+ 1", command=geklickt_2)
btn_2.grid(column=3, row=1, padx=10, pady=10)

anzeige = Label(fenster, text="Anzeigentext134rwwr")
anzeige.grid(column=1, row=2, padx=10, pady=10)

anzeige_2 = Label(fenster, text="Hallo wie gehts?")
anzeige_2.grid(column=1, row=15, padx=10, pady=10)

