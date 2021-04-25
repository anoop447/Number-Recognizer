from tkinter import *
from tkinter import messagebox
import cv2 as cv
from PIL import ImageGrab,Image
import numpy as np
import pygetwindow as gw
import tensorflow as tf

lasx = None
lasy = None

app = Tk()
app.geometry('400x400')



def get_x_y(event):
    global lasx, lasy
    lasx,lasy = event.x,event.y

def draw(event):
    global lasx, lasy
    canvas.create_line((lasx,lasy,event.x,event.y),width=15)
    lasx , lasy = event.x,event.y


def ss(event):
    model = tf.keras.models.load_model('predictors.model')
    win = gw.getWindowsWithTitle('tk')[0]
    winleft = win.left+9
    wintop = win.top+38 #change 38 to 7 to not capture the titlebar
    winright = win.right-9
    winbottom = win.bottom-9
    final_rect = (winleft,wintop,winright,winbottom)
    img = ImageGrab.grab(final_rect)
    new_img = img.resize((28,28),Image.ANTIALIAS)   

    new_img.save('img.png',optimize=True,quality=95)

    #img = save_as_png(canvas,'img')
    img = cv.imread('img.png')[:,:,0]
    
    img = np.invert(np.array([img]))
    
    prediction = model.predict(img)
    t = (np.argmax(prediction))
    messagebox.showinfo("Prediction", "I predict this number as : " + str(t))



canvas = Canvas(app,bg='white')
canvas.pack(anchor='nw',fill='both',expand=1)

canvas.bind('<Button-1>',get_x_y)
canvas.bind('<B1-Motion>',draw)
app.bind('<Return>',ss)


app.mainloop()