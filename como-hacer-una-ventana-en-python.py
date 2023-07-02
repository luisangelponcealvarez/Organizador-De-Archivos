from tkinter import *


def mensaje():
    print("mensaje del boton")


ventana = Tk()
ventana.title("creando una ventana con python")
ventana.geometry("600x600")

lbl = Label(ventana, text="creando button con python")
lbl.pack()

btn = Button(ventana, text="presiona este [button] para mensaje", command=mensaje)
btn.pack()

ventana.mainloop()
