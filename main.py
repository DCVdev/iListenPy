from lib2to3.pgen2.literals import evalString
import os,sys,glob
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from functools import partial
import pygame 
#Inicio de pygame
pygame.init()
#Inicio del Frame
root = Tk()
frm = ttk.Frame(root)
frm.grid()
#Se crea las variables que servirán para posicionar las imágenes y botones y para guardarlas en arrays
posx=0
posy=0
x=0
y=1
musicas=[]
imgsbotons=[]
imagenes=[]
btns=[]
i=0
#Función que carga las canciones
def cargarCancion(music):
    musicas.append(music)
#Función que reproduce las canciones
def playCancion(btn):
    z = int(btn)
    btns.append(z)
    pygame.mixer.music.load(musicas[z])
    pygame.mixer.music.play()
#Función que inserta la imagen en el frame
def displayImg(img,z):
    image = Image.open(img)
    imagen = image.resize((100,100))
    photo = ImageTk.PhotoImage(imagen)
    imagenes.append(photo)#keep references
    texto=str(z)
    newPhoto_label = Button(image=photo,text=texto)
    newPhoto_label.configure(command=partial(playCancion,texto))
    #Borramos lo innecesario para que se quede limpio
    imgi=img[5:]
    imgii=imgi.replace('.jpg'," ")
    photo_txt = Label(text=imgii)
    newPhoto_label.grid(column=posx,row=posy)
    photo_txt.grid(column=x,row=y)
#Función que añade el botón de reproducir
def botonPlay(z):
    btnplay = Image.open(z)
    imagez= btnplay.resize((50,50))
    play=ImageTk.PhotoImage(imagez)
    imgsbotons.append(play)
    playtbn=Button(image=play,command=reproducir)
    playtbn.grid(column=x,row=y)
#Función que añade el botón de pausa
def botonPause(z):
    btnpause = Image.open(z)
    imagez= btnpause.resize((50,50))
    pause=ImageTk.PhotoImage(imagez)
    imgsbotons.append(pause)
    pausebtn=Button(image=pause,command=pausar)
    pausebtn.grid(column=x,row=y)
#Función que añade el botón de siguiente
def botonSiguiente(z):
    btnsiguiente = Image.open(z)
    imagez= btnsiguiente.resize((50,50))
    siguiente=ImageTk.PhotoImage(imagez)
    imgsbotons.append(siguiente)
    siguientebtn=Button(image=siguiente,command=siguientes)
    siguientebtn.grid(column=x,row=y)
#Función que añade el botón de anterior
def botonAnterior(z):
    btnanterior = Image.open(z)
    imagez= btnanterior.resize((50,50))
    anterior=ImageTk.PhotoImage(imagez)
    imgsbotons.append(anterior)
    anteriorbtn=Button(image=anterior,command=anteriores)
    anteriorbtn.grid(column=x,row=y)
#Función que añade el botón de stop
def botonStop(z):
    btnstop = Image.open(z)
    imagez= btnstop.resize((50,50))
    stop=ImageTk.PhotoImage(imagez)
    imgsbotons.append(stop)
    stopbtn=Button(image=stop,command=stoping)
    stopbtn.grid(column=x,row=y)
#Función que añade el botón de volumen
def botonVolumen(z):
    btnvolumen = Image.open(z)
    imagez= btnvolumen.resize((50,50))
    volumen=ImageTk.PhotoImage(imagez)
    imgsbotons.append(volumen)
    volumenbtn=Button(image=volumen, command=partial(volumen1,volumen))
    volumenbtn.grid(column=x,row=y)
#Función que pausa las canciones
def pausar():
    pygame.mixer.music.pause()
#Función que reproduce las canciones
def reproducir():
    pygame.mixer.music.unpause()
#Función que para la canción
def stoping():
    pygame.mixer.music.stop()
#Función que actualiza el volumen de la canción
def volumen1(volumenbtn):
    frmvol=ttk.Frame(volumenbtn)
    frmvol.grid()
    s = pygame.mixer.music.get_volume()
    print(s)
#Funcion que pasa a la siguiente canción
def siguientes():
   if(len(btns)<1): 
        z=btns[0]
   else:
        z=btns[-1]
        z+=1
   pygame.mixer.music.load(musicas[z]) 
   pygame.mixer.music.play() 
   btns.append(z)
  
#Función que pasa a la anterior canción
def anteriores():
   if(len(btns)<1): 
        z=btns[0]
   else:
        z=btns[-1]
        z-=1
   pygame.mixer.music.load(musicas[z]) 
   pygame.mixer.music.play() 
   btns.append(z)
#bucle que lee las imágenes de las canciones y llama a la función para poner las imagenes en el frame
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
#bucle que lee las canciones y llama a la función para poner las canciones en las imágenes
for m in glob.glob("music/*.mp3"):
        cargarCancion(m)    
#bucle que lee los botones y tiene condicionales para saber que botón poner y luego llama a la función   
for img in glob.glob("imgbtn/*.jpg"):   
    if(img=="imgbtn\play.jpg"):
        botonPlay(img)
        x+=1
    elif(img=="imgbtn\pause.jpg"):
        botonPause(img)
        x+=1
    elif(img=="imgbtn\sefore.jpg"):
        botonAnterior(img)
        x+=1
    elif(img=="imgbtn\siguiente.jpg"):
        botonSiguiente(img)
        x+=1
    elif(img=="imgbtn\stop.jpg"):
        botonStop(img)
        x+=1
    elif(img=="imgbtn\solumen.jpg"):
        botonVolumen(img)
        x+=1
root.mainloop()