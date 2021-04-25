from tkinter import *
lasx = None
lasy = None

app = Tk()
app.geometry('400x400')



def get_x_y(event):
    global lasx, lasy
    lasx,lasy = event.x,event.y

def draw(event):
    global lasx, lasy
    canvas.create_line((lasx,lasy,event.x,event.y),width=10)
    lasx , lasy = event.x,event.y


canvas = Canvas(app)
canvas.pack(anchor='nw',fill='both',expand=1)

canvas.bind('<Button-1>',get_x_y)
canvas.bind('<B1-Motion>',draw)


app.mainloop()