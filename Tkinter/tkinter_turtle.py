from tkinter import *
import turtle

fenster = Tk()

fenster.title("Neues Fenster hoffentlich mit Turtle")

canvas = Canvas(master = fenster, width = 600, height = 600)

canvas.pack()

reinhard = turtle.RawTurtle(canvas)



############################################################
canvas.pack()

def main():
    canvas.bind_all("<KeyPress-Up>",moveretangle)
    canvas.bind_all("<KeyPress-Down>",moveretangle)
    canvas.bind_all("<KeyPress-Left>",moveretangle)
    canvas.bind_all("<KeyPress-Right>",moveretangle)
    canvas.bind_all("<KeyPress-k>",moveretangle)
    canvas.bind_all("<KeyPress-q>",moveretangle)
    
    print("Hallo")
    fenster.mainloop()


x = 0
y = 0
q_variable = 0    
def moveretangle(event):
    global x
    global y
    global q_variable
    
    if event.keysym == 'Up':
        reinhard.sety(y+10)
        y += 10
    elif event.keysym == 'Down':
         reinhard.sety(y-10)
         y -= 10
    elif event.keysym == 'Left':
        reinhard.setx(x-10)
        x -= 10
    elif event.keysym == 'Right':
        reinhard.setx(x+10)
        x += 10
    elif event.keysym == 'k':
        print("k")
        kreis()
    elif event.keysym == 'q':
        shape_liste = ["turtle", "square","circle", "triangle", "classic", "arrow"]
        print("q_variable->",q_variable%len(shape_liste))
        reinhard.shape(shape_liste[q_variable%len(shape_liste)])
        q_variable += 1
        
    else:
        pass

##################################################################    
    
def forward_btn():
   
    reinhard.forward(10)

    
def rot():
    reinhard.color("red")
    
def schwarz():
    reinhard.color("black")


def pink():
    reinhard.color("pink")

def blue():
    reinhard.color("blue")

def yellow():
    reinhard.color("yellow")

def purple():
    reinhard.color("purple")

def right():
    reinhard.right(90)  

def left():
    reinhard.left(90)
    
def p_up():
    reinhard.pu()
    
def p_down():
    reinhard.pd()

w = 1
def turtle_width_p():
    global w
    w = w + 1
    reinhard.width(w)
    
def turtle_width_m():
    global w
    if w >= 2:
        w = w - 1
    else:
        w = 1
    reinhard.width(w)

# loeschfunktion
def delete():
    reinhard.clear()

def quadrat(weite=100):
    for i in range(4):
        reinhard.forward(weite)
        reinhard.right(90)

def kreis():
    reinhard.circle(30)

button_1 = Button(fenster, text="vowärts", command=forward_btn).pack(side = LEFT)
button_1_b = Button(fenster, text="width +1", command=turtle_width_p).pack(side = LEFT)
button_1_c = Button(fenster, text="width -1", command=turtle_width_m).pack(side = LEFT)
button_up = Button(fenster, text="up", command=p_up).pack(side = LEFT)
button_down = Button(fenster, text="down", command=p_down).pack(side = LEFT)

button_2 = Button(fenster, text="red", background = 'red', command=rot).pack(side = RIGHT)
button_3 = Button(fenster, text="black", command=schwarz).pack(side = RIGHT)
button_4 = Button(fenster, text="pink", background = 'pink', command=pink).pack(side = RIGHT)
button_5 = Button(fenster, text="blue", background = 'blue', command=blue).pack(side = RIGHT)
button_6 = Button(fenster, text="yellow", command=yellow).pack(side = RIGHT)
button_7 = Button(fenster, text="purple", command=purple).pack(side = RIGHT)
button_8 = Button(fenster, text="right", command=right).place(x=40, y=520)
##button_9 = Button(fenster, text="left", command=left).pack(side = RIGHT)
button_9 = Button(fenster, text="left", command=left).place(x=120, y=520)

# erstelle button zum löschen
button_delete = Button(fenster, text="delete", command=delete).pack(side = LEFT)

button_quadrat = Button(fenster, text="quadrat", command=quadrat).pack(side = LEFT)

main()
fenster.mainloop()

##if __name__ == '__main__':
##    main()
