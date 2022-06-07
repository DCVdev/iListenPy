from email.mime import audio
import os,sys,glob
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from mutagen.mp3 import MP3
import pygame
pygame.init()

posx=0
posy=0
x =0
y=1
musicas=[]
xmusic=()
i=0
imagenes=[]
class app:
    def generarVentana():
        root = Tk()
        frm = ttk.Frame(root)
        frm.grid()
        root.mainloop()
    def cajaImagen(img):
        image = Image.open(img)
        imagen = image.resize((100,100))
        photo = ImageTk.PhotoImage(imagen)
        imagenes.append(photo)#keep references
        newPhoto_label = Button(image=photo)
        photo_txt = Label(text=img)
        newPhoto_label.grid(column=posx,row=posy)
        photo_txt.grid(column=x,row=y)

    def cajaMusica(music):
        musicas.append(music)
        audio=musicas[i]
        pygame.mixer.music.load(audio)
clase= app
for mp3 in glob.glob("music/*.mp3"):
    clase.cajaMusica(mp3)
    
for files in glob.glob("imgs*.*"):
    clase.cajaImagen(files)
    posx= posx+1
    x=x+1
    if(posx==6):
        posy=posy +2
        posx=0
        x=0
        y=y+2

clase.generarVentana()
        
