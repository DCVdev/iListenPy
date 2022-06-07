from lib2to3.pgen2.literals import evalString
import os,sys,glob
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from functools import partial
import pygame 
pygame.init()
root = Tk()
frm = ttk.Frame(root)
frm.grid()
posx=0
posy=0
x =0
y=1
musicas=[]
xmusic=[]
i=0
def cargarCancion(music):
    musicas.append(music)
def playCancion(btn):
    z = int(btn)
    pygame.mixer.music.load(musicas[z])
    pygame.mixer.music.play()
for m in glob.glob("music/*.mp3"):
    cargarCancion(m)
imagenes=[]
def displayImg(img,z):
    image = Image.open(img)
    imagen = image.resize((100,100))
    photo = ImageTk.PhotoImage(imagen)
    imagenes.append(photo)#keep references
    texto=str(z)
    newPhoto_label = Button(image=photo,text=texto)
    newPhoto_label.configure(command=partial(playCancion,texto))
    photo_txt = Label(text=img)
    newPhoto_label.grid(column=posx,row=posy)
    photo_txt.grid(column=x,row=y)
for f in glob.glob("imgs/*.*"):
    displayImg(f,i)
    if(i<29):
        i+=1
    posx+=1
    x+=1
    if(posx==6):
        posy+=2
        posx=0
        x=0
        y+=2
        
"""for img in glob.glob("")
def cargarBotones():
    zet = "imgbtn/play.jpg"
    images = Image.open(zet)
    imagez= images.resize((50,50))
    play=ImageTk.PhotoImage(imagez)
    playtbn=Button(image=play)
    playtbn.grid(column=x,row=y)
cargarBotones()"""
root.mainloop()