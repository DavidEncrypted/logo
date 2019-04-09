from tkinter import *
from PIL import ImageTk, Image, ImageDraw
import os

x1 = 0
y1 = 0
x2 = 0
y2 = 0

root = Tk()
img = ImageTk.PhotoImage(Image.open("./frames/frame300.jpg"))

canvas = Canvas(root, height=img.height(), width=img.width())
canvas.pack()
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.create_line(0, 200, 399, 200, dash=(2,2))  # x-axis
rec = canvas.create_rectangle(x1, y1, x2, y2, fill='red')
def onCanvasClick(event):
    print('Got canvas click', event.x, event.y, event.widget)
    global x1
    x1 = event.x
    global y1
    y1 = event.y
    print(x1,y1)

def onCanvasRelease(event):
    print('Got canvas release', event.x, event.y, event.widget)
    global x1
    global y1
    global x2
    global y2
    x2 = event.x
    y2 = event.y
    global rec
    print(canvas.coords(rec))
    t1, u1, t2, u2 = canvas.coords(rec)
    t1 = x1
    u1 = y1
    t2 = x2
    u2 = y2
    canvas.coords(rec, t1,u1,t2,u2)
    print(canvas.coords(rec))
    #panel.move(rec, 0, 0)

def onEnter(event):
	print("ENTER")
	maskimg = Image.new('RGB', (img.width(), img.height()), color = 'black')
	draw = ImageDraw.Draw(maskimg)
	draw.rectangle([x1,y1,x2,y2], fill="white")
	maskimg.save('masktest.png')

canvas.bind("<Button-1>", onCanvasClick)
canvas.bind("<ButtonRelease-1>", onCanvasRelease)
root.bind("<Return>", onEnter)
root.mainloop()