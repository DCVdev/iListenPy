from tkinter import *
from PIL import Image, ImageTk
import glob, os

root = Tk()
root.geometry("800x600")

photos = []

def displayImg(img):
    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)
    photos.append(photo)#keep references!
    newPhoto_label = Label(image=photo)
    newPhoto_label.pack()

for file in glob.glob("imgs/*jpg"):
    displayImg(file)
    print(file)
   

imagenes=[]

def displayImg(img):
    image = Image.open(img)
    photo = ImageTk.PhotoImage(image)
    imagenes.append(photo)#keep references!
    newPhoto_label = Label(image=photo)
    newPhoto_label.pack()

for f in glob.glob("imgs/*jpg"):
    displayImg(f)
    print(f)
    
    
imagenes=[]
for f in files:
    imagenes.append(f)
for img in imagenes:
    imagen=Image.open(dir+img)
    print(img)
    img = imagen.resize((100,100))
    my_img=ImageTk.PhotoImage(img)
    panel=Label(frm,image=my_img)
    panel.grid(row=posx,column=posy)
    posx=posx +1
    if(posx/10==1):
        posy+1
        pos
        
        

root.mainloop()