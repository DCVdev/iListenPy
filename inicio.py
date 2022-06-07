import tkinter as tk

ventana = tk.Tk()

frame1 = tk.Frame(master=ventana, width=100,height=100, bg="red")
frame1.pack()

frame2 = tk.Frame(master=ventana, width=50, height=50, bg="yellow")
frame2.pack()

frame3=tk.Frame(master=ventana, width=25, height=25, bg="blue")
frame3.pack()

ventana.mainloop()