from cProfile import label
from calendar import c
from cgitb import text
from inspect import Parameter
from re import T
from tkinter import* 
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk


root = Tk()
root.title('iListener')


#width="500" , height="650"
root.geometry("600x650")


#Iniciar Pygame 
pygame.mixer.init()
    

# Coger información de tiempo de duración de la canción
def tiempo_cancion():

    if parar:  
        return 

    tiempo_actual=pygame.mixer.music.get_pos() / 1000


    #OBTENER DATOS 
    #slider_label.config(text=f'slider: {int(mi_slider.get())} Y posicion de la canción: {int(tiempo_actual)}')
    #Convertir el tiempo en un formato
    convertir_tiempo_actual = time.strftime('%M:%S',time.gmtime(tiempo_actual))


 #obtener la canción que se está reproduciendo actualmente
    cancion_actual = caja_cancion.curselection()

    #coger la lista sde reproducción del formulario del título de la canción
    cancion = caja_cancion.get(cancion_actual)

    #estructura de directorio y titulo de la cancion en MP3
    cancion= f'music/{cancion}.mp3'


    #obtener la duración de la canción con Mutagen ( pip install mutagen)
    cancion_mut= MP3(cancion)

    global duracion_cancion
    duracion_cancion=cancion_mut.info.length

    #convertir el formato
    convertir_duracion_cancion=time.strftime('%M:%S',time.gmtime(duracion_cancion))



    #Incrementar el tiempo por un segundo
    tiempo_actual +=1

    if int(mi_slider.get()) == int(duracion_cancion):
        barra.config(text=f'Tiempo Canción:  {convertir_duracion_cancion}')
    
    elif paused:
        pass 

    elif int(mi_slider.get()) == int(tiempo_actual):
        #Actualizar la posicion del Slide
        posicion_slide=int(duracion_cancion)
        mi_slider.config(to=posicion_slide, value=int(tiempo_actual))
    else: 
        #Slider tiene que moverse
        posicion_slide=int(duracion_cancion)
        mi_slider.config(to=posicion_slide, value=int(mi_slider.get()))

        convertir_tiempo_actual = time.strftime('%M:%S',time.gmtime(int(mi_slider.get())))

        barra.config(text=f'Tiempo Canción: {convertir_tiempo_actual} de {convertir_duracion_cancion}')

        # Mover por un segundo
        siguiente_tiempo=int(mi_slider.get()) +1
        mi_slider.config(value=siguiente_tiempo)

#REdondear los segundos del tiempo de la canción
    #barra.config(text=f'Tiempo Canción: {convertir_tiempo_actual} de {convertir_duracion_cancion}')

    #posicion el slide con la canción
    # ---- mi_slider.config(value=int(tiempo_actual)) ----

 #Actualzar la posicion del slider
  #  posicion_slide=int(duracion_cancion)
   # mi_slider.config(to=posicion_slide, value=int(tiempo_actual))

#Actualización del tiempo
    barra.after(1000,tiempo_cancion)



# Añadir canciones (FUNCIONES)
# **** AÑADE OTRA CANCIÓN ABRIENDO EL ARCHIVO LOCAL ****
def añadir_cancion():
    cancion= filedialog.askopenfilename(initialdir='music/' , title="Elige una canción", filetypes=(("mp3 files", "*.mp3"),))

    # ********  QUITAR INFORMACIÓN DEL DIRECTORIO QUE SALE EN LA CAJA DE CANCIÓN **********
    cancion= cancion.replace("music/","")
    cancion= cancion.replace(".mp3","")

    # Añadir canción a la caja de la lista.
    caja_cancion.insert(END,cancion)

#AÑADIR CANCIONES A LA PLAYLIST
def añadir_canciones():
    canciones= filedialog.askopenfilenames(initialdir='canciones/' , title="Elige una canción", filetypes=(("mp3 files", "*.mp3"),))
    #recorrer la lista de canciones y reemplazar la información del directorio y el mp3
    for cancion in canciones:
        cancion= cancion.replace("C:/Users/andre/Downloads/Andre Proyectos/Python MP3/Canciones/","")
        cancion= cancion.replace(".mp3","")
    #INTRODUCIRLO A LA PLAYLIST
        caja_cancion.insert(END,cancion)


#Seleccionar y reproducir la canción
def play():

    global parar
    parar = False
    cancion= caja_cancion.get(ACTIVE)
    cancion= f'music/{cancion}.mp3'

    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=0)

    #Pausar en el mismo boton de PLAY (PRUEBAS)
    #   pygame.mixer.music.pause()
    #  pygame.mixer.music.unpause()

    #llamar a tiempo canción
    tiempo_cancion()

    #Actualzar la posicion del slider
    #posicion_slide=int(duracion_cancion)
    #mi_slider.config(to=posicion_slide, value=0)

    #obtiene el tiempo actual del volumen (numero)
    volumen_actual=pygame.mixer.music.get_volume()
    slider_label.config(text=volumen_actual * 100)

global parar
parar=False
# *** #Seleccionar y reproducir la canción *** 
def stop():
    #resetear el Slide y la barra
    barra.config(text='')
    mi_slider.config(value=0)
    #Parar cancion
    pygame.mixer.music.stop()
    caja_cancion.select_clear(ACTIVE)

    #limpiar la barra
    barra.config(text='')

    #Variable para parar
    global parar
    parar= True


def siguiente_cancion():
    # Obtener el número de tupla de la canción actual
    siguientes = caja_cancion.curselection()
    # agregar uno al número de canción actual 
    siguientes=siguientes[0]+1

    cancion = caja_cancion.get(siguientes)

    #Añadir estructura de directorio y titulo de la cancion en MP3
    cancion= f'music/{cancion}.mp3'
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=0)

    #Mover la barra en la playlist 
    caja_cancion.selection_clear(0,END)

    #Activar la barra con la nueva canción
    caja_cancion.activate(siguientes)

    # Seguimiento de la barra a la siguiente canción
    caja_cancion.selection_set(siguientes, last=None)



# **** CANCION ANTERIOR  de la playlist **** 

def cancion_anterior():

    barra.config(text='')
    mi_slider.config(value=0)

     # Obtener el número de tupla de la canción actual
    siguientes = caja_cancion.curselection()
    # agregar uno al número de canción actual 
    siguientes=siguientes[0]-1

    cancion = caja_cancion.get(siguientes)

    #Añadir estructura de directorio y titulo de la cancion en MP3
    cancion= f'music/{cancion}.mp3'
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=0)

    #Mover la barra en la playlist 
    caja_cancion.selection_clear(0,END)

    #Activar la barra con la nueva canción
    caja_cancion.activate(siguientes)

    # Seguimiento de la barra a la siguiente canción
    caja_cancion.selection_set(siguientes, last=None)


#************* ELIMINAR UNA CANCION ***************
def eliminar_cancion():
    stop()
    caja_cancion.delete(ANCHOR)
    #Para la cancion si está reproduciendose
    pygame.mixer.music.stop()

# ELIMINAR TODAS LAS CANCIONES DE LA PLAYLIST
def eliminar_canciones():
    stop()
    caja_cancion.delete(0 , END)
    #para la musica si es que se está reproduciendo
    pygame.mixer.music.stop()

 # CREAR UNA VARIABLE DE PAUSA GLOBAL
global paused
paused = False

# PAUSAR LA CANCIÓN
def pause(esta_pausado):
    global paused
    paused=esta_pausado

    if paused: 
      # REANADUAR
      pygame.mixer.music.unpause()    
      paused=False
    else:  
      #Pause
      pygame.mixer.music.pause()
      paused=True

 # ***************************  Creamos el Slide *******************************
def slide(X):
    cancion= caja_cancion.get(ACTIVE)
    cancion= f'music/{cancion}.mp3'

    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(loops=0,start=int(mi_slider.get()))


# *************************** Crear la funcion volument ******************************
def volume(x):
    pygame.mixer.music.set_volume(volumen_slide.get())

    #volumen_actual=pygame.mixer.music.get_volume()
    #slider_label.config(text=volumen_actual * 100)

    #slider_label.config(text=f'{int(mi_slider.get())} de {int(duracion_cancion)}')
# CREAR VOLUMEN
volumen= Frame(root)
volumen.pack(pady=20)

#Creamos la caja de PLaylist
caja_cancion= Listbox(volumen, bg="black", fg="white", width=80,height=20, selectbackground="gray", selectforeground="white")
caja_cancion.grid(row=0, column=0)

# Definir los controles de botonoes en imagenes.
volver_btn_img = PhotoImage(file='imgtbn/sefore.jpg')
play_btn_img = PhotoImage(file='imgbtn/play.jpg')
siguiente_btn_img = PhotoImage(file='imgbtn/siguiente.jpg')
pausar_btn_img = PhotoImage(file='imgbtn/pause.')
cerrar_btn_img = PhotoImage(file='imageness/stop.png')

# Crear el control de botones (VENTANA)
controls_frame = Frame(volumen)
controls_frame.grid(row=1, column=0, pady=20)

#Crear Volumen label Frame
volumen_frame= LabelFrame(volumen, text="Volumen")
volumen_frame.grid(row=0,column=1,padx=20)

# Crear El boton con 
volver_btn = Button(controls_frame, image=volver_btn_img, borderwidth=0, command=cancion_anterior)
play_btn = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play )
pausar_btn = Button(controls_frame, image=pausar_btn_img, borderwidth=0, command=lambda: pause(paused))
siguiente_btn = Button(controls_frame, image=siguiente_btn_img, borderwidth=0, command=siguiente_cancion)
cerrar_btn = Button(controls_frame, image=cerrar_btn_img, borderwidth=0,  command=stop)

# POSICION DE LOS BOTONES
cerrar_btn.grid(row=0,column=0, padx=10)
volver_btn.grid(row=0,column=1, padx=10)
play_btn.grid(row=0,column=2, padx=10)
siguiente_btn.grid(row=0,column=3, padx=10)
pausar_btn.grid(row=0,column=4, padx=10)

# Crear el Menú
mi_menu= Menu(root)
root.config(menu=mi_menu)

# Añadir una cancion al menu
añadir_cancion_menu= Menu(mi_menu)
mi_menu.add_cascade(label="Añadir canciones", menu=añadir_cancion_menu)
añadir_cancion_menu.add_command(label="Añadir una canción a la Playlist", command=añadir_cancion)

#Añadir mas de una canción a la playlist
añadir_cancion_menu.add_command(label="Añadir mas canciones a la Playlist", command=añadir_canciones)


#ELIMINAR ALGUNA CANCION (MENU)

eliminar_cancion_menu= Menu(mi_menu)
mi_menu.add_cascade(label="Eliminar canciones",menu=eliminar_cancion_menu)
eliminar_cancion_menu.add_command(label="Eliminar una canción de la Playlist", command=eliminar_cancion)
eliminar_cancion_menu.add_command(label="Eliminar todas las canciones de la Playlist",command=eliminar_canciones)

#Crear barra de reproducción
barra= Label(root, text='', bd=1,relief=GROOVE,anchor=E)
barra.pack(fill=X, side=BOTTOM, ipady=2)

#BARRA SLIDE 

mi_slider=ttk.Scale(volumen, from_=0, to=100, orient=HORIZONTAL, value=0, command=slide, length=360)
mi_slider.grid(row=2, column=0, pady=10)

# CREAR EL SLIDE DEL VOLUMEN
volumen_slide=ttk.Scale(volumen_frame, from_=0, to=1, orient=VERTICAL, value=1, command=volume , length=125)
volumen_slide.pack(pady=20)

#Crear un slider temporal
slider_label=Label(root,text="0")
slider_label.pack(pady=10)

root.mainloop()