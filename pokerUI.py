import tkinter

def test():
    window = tkinter.Tk()
    window.title("Poker")
    tableFrame = tkinter.Frame(window).pack()
    handFrame = tkinter.Frame(window).pack(side = "bottom")
    tkinter.Label(window, text = take("standin"), fg = "black", bg = "white").pack()
    window.mainloop()

def give(thing):
    take(thing)

def take(thing):
    return thing
