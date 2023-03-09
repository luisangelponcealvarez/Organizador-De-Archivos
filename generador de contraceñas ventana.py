from random import *
from tkinter import *

""" ventana """

ventana = Tk()
ventana.title("generador de contraseñas")
ventana.geometry("600x600")

lbl = Label(ventana, text="generador de contraseñas")
lbl.pack()

btn = Button(
    ventana, text="presiona este button para generar una contraseña aleatoria",
    command="p"
)
btn.pack()

ventana.mainloop()

""" generador """

longitud = 20
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
p=""
p=p.join([choice(valores)for i in range(longitud)])

