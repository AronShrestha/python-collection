import tkinter
import _tkinter

HEIGHT = 700
WIDTH = 800

root = tkinter.Tk()

canvas = tkinter.Canvas(root, height = HEIGHT, width=WIDTH)
canvas.pack()

frame = tkinter.Frame(root, bg='red')
frame.pack()

root.mainloop()