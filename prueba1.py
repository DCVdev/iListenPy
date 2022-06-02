from tkinter import *
from PIL import Image, ImageTk
import glob, os
from functools import partial
import tkinter as tk



def db_view_data(boton):
    print(boton["text"])


root = tk.Tk()
root.geometry("400x300")


for n in range(10):
    texto = str(n)
    boton = tk.Button(root, text=texto)
    boton.configure(command=partial(db_view_data, boton))
    boton.pack()

root.mainloop()