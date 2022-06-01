 #! /usr/bin/python3

from distutils.log import error

import glob
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import glob,os
##  ImportError: cannot import name 'ImageTk' from 'PIL'
##  pip3 install --upgrade --force-reinstall pillow
##~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


musica=[]
for m in glob.glob("music/*.mp3"):
    musica.append(m)
    print (m)