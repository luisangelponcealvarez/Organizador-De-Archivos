import os
import shutil
import customtkinter as ctk
from tkinter import filedialog, messagebox, StringVar
from tkinter import *


def seleccionar_carpeta():
    directorio = filedialog.askdirectory()
    return directorio


def organizar_archivos(directorio, tipo_archivo):
    for filename in os.listdir(directorio):
        if tipo_archivo == "Imagenes" and (
            filename.endswith(".jpg") or filename.endswith(".png")
        ):
            if not os.path.exists(directorio + "/Imagenes"):
                os.makedirs(directorio + "/Imagenes")
            shutil.move(
                directorio + "/" + filename, directorio + "/Imagenes/" + filename
            )
        elif tipo_archivo == "Videos" and filename.endswith(".mp4"):
            if not os.path.exists(directorio + "/Videos"):
                os.makedirs(directorio + "/Videos")
            shutil.move(directorio + "/" + filename, directorio + "/Videos/" + filename)
        elif tipo_archivo == "Audios" and filename.endswith(".mp3"):
            if not os.path.exists(directorio + "/Audios"):
                os.makedirs(directorio + "/Audios")
            shutil.move(directorio + "/" + filename, directorio + "/Audios/" + filename)
        elif tipo_archivo == "Documentos" and (
            filename.endswith(".docx") or filename.endswith(".pdf")
        ):
            if not os.path.exists(directorio + "/Documentos"):
                os.makedirs(directorio + "/Documentos")
            shutil.move(
                directorio + "/" + filename, directorio + "/Documentos/" + filename
            )


root = Tk()
root.geometry("200x200")

tipo_archivo = StringVar()
tipo_archivo.set("Imagenes")  # valor inicial

boton_carpeta = ctk.CTkButton(
    root, text="Seleccionar carpeta", command=seleccionar_carpeta
)
boton_carpeta.pack()

opcion_imagenes = Radiobutton(
    root, text="Imágenes", variable=tipo_archivo, value="Imagenes"
)
opcion_imagenes.pack()

opcion_videos = Radiobutton(root, text="Videos", variable=tipo_archivo, value="Videos")
opcion_videos.pack()

opcion_audios = Radiobutton(root, text="Audios", variable=tipo_archivo, value="Audios")
opcion_audios.pack()

opcion_documentos = Radiobutton(
    root, text="Documentos", variable=tipo_archivo, value="Documentos"
)
opcion_documentos.pack()

boton_organizar = ctk.CTkButton(
    root,
    text="Organizar",
    command=lambda: organizar_archivos(seleccionar_carpeta(), tipo_archivo.get()),
)
boton_organizar.pack()

root.mainloop()
