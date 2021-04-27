from tkinter import *
from tkinter import messagebox
import cv2 as cv
from PIL import ImageGrab,Image
import numpy as np
import tensorflow as tf


lasx = None
lasy = None
model = tf.keras.models.load_model('predictors.model')
app = Tk()
app.geometry('400x400')

def get_x_y(event):
    global lasx, lasy
    lasx,lasy = event.x,event.y

def draw(event):
    global lasx, lasy
    canvas.create_line((lasx,lasy,event.x,event.y),width=15)
    lasx , lasy = event.x,event.y

def clear(event):
    canvas.delete("all")

def getter(widget):
    x=app.winfo_rootx()+widget.winfo_x()
    y=app.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    img = ImageGrab.grab().crop((x,y,x1,y1))
    new_img = img.resize((28,28),Image.ANTIALIAS)
    new_img.save('img.png',optimize=True,quality=95)
        

def ss(event):
    
    getter(app)

    img = cv.imread('img.png')[:,:,0]
    img = np.invert(np.array([img]))
    
    prediction = model.predict(img)
    t = (np.argmax(prediction))
    
    messagebox.showinfo("Prediction", "I predict this number as : " + str(t))
    



canvas = Canvas(app,bg='white')
canvas.pack(anchor='nw',fill='both',expand=1)

canvas.bind('<Button-1>',get_x_y)
canvas.bind('<B1-Motion>',draw)
app.bind('<space>',clear)
app.bind('<Return>',ss)


app.mainloop()

