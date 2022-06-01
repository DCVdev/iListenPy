from email.mime import audio
import os,sys,glob
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from mutagen.mp3 import MP3
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
xmusic=()
i=0
"""def displayMusic(audio):
    musicas.append(audio)
    pygame.mixer.music.load(musicas[xmusic])
    pygame.mixer.music.play()"""

    

"""def playCancion(music):
    pygame.mixer.music.load(musicas[i])"""

"""for m in glob.glob("music/*.mp3"):
    playCancion(m)
    musicas.append(m)
    """
imagenes=[]
def displayImg(img):
    image = Image.open(img)
    imagen = image.resize((100,100))
    photo = ImageTk.PhotoImage(imagen)
    imagenes.append(photo)#keep references
    newPhoto_label = Button(image=photo)
    photo_txt = Label(text=img)
    newPhoto_label.grid(column=posx,row=posy)
    photo_txt.grid(column=x,row=y)

for f in glob.glob("imgs/*.*"):
    displayImg(f)
    posx= posx+1
    x=x+1
    if(posx==6):
        posy=posy +2
        posx=0
        x=0
        y=y+2

  
root.mainloop()

