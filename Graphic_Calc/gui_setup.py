from tkinter import *

class SetUpGUI:

    def __init__(self):
        
        gui = Tk()
        gui.geometry("200x200")

        expression = Entry(gui)
        expression.grid(row=4, column=0, columnspan=6)

        button_1 = Button(gui, text = "1", height = 2, width = 4)
        button_1.grid(row=0, column=0)

        button_2 = Button(gui, text = "2", height = 2, width = 4)
        button_2.grid(row=0, column=1)

        button_3 = Button(gui, text = "3", height = 2, width = 4)
        button_3.grid(row=0, column=2)

        button_4 = Button(gui, text = "4", height = 2, width = 4)
        button_4.grid(row=1, column=0)

        button_5 = Button(gui, text = "5", height = 2, width = 4)
        button_5.grid(row=1, column=1)

        button_6 = Button(gui, text = "6", height = 2, width = 4)
        button_6.grid(row=1, column=2)

        button_7 = Button(gui, text = "7", height = 2, width = 4)
        button_7.grid(row=2, column=0)

        button_8 = Button(gui, text = "8", height = 2, width = 4)
        button_8.grid(row=2, column=1)

        button_9 = Button(gui, text = "9", height = 2, width = 4)
        button_9.grid(row=2, column=2)

        button_0 = Button(gui, text = "0", height = 2, width = 4)
        button_0.grid(row=3, column=1)

        button_add = Button(gui, text = "+", height = 2, width = 4)
        button_add.grid(row=0, column=4)

        button_sub = Button(gui, text = "-", height = 2, width = 4)
        button_sub.grid(row=0, column=5)

        button_mult = Button(gui, text = "x", height = 2, width = 4)
        button_mult.grid(row=1, column=4)

        button_div = Button(gui, text = "/", height = 2, width = 4)
        button_div.grid(row=1, column=5)

        button_deci = Button(gui, text = ".", height = 2, width = 4)
        button_deci.grid(row=2, column=4)

        button_equals = Button(gui, text = "=", height = 2, width = 4)
        button_equals.grid(row=2, column=5)

        button_C = Button(gui, text = "C", height = 2, width = 4, fg = 'black')
        button_C.grid(row=3, column=0)

        gui.mainloop()

