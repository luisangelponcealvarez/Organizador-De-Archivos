import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from pytube import YouTube

def seleccionar_carpeta():
    carpeta = filedialog.askdirectory()
    carpeta_destino.set(carpeta)

def descargar_audio():
    url = entrada.get()
    carpeta = carpeta_destino.get()

    try:
        video = YouTube(url)
        audio_stream = video.streams.filter(only_audio=True).first()
        audio_stream.download(output_path=carpeta)
        messagebox.showinfo("Descarga completa", "El audio se ha descargado correctamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

ventana = tk.Tk()
ventana.title("Descargador de Audios")
ventana.geometry("400x250")

etiqueta_url = tk.Label(ventana, text="Ingrese la URL del video de YouTube:")
etiqueta_url.pack()

entrada = tk.Entry(ventana, width=50)
entrada.pack()

etiqueta_carpeta = tk.Label(ventana, text="Carpeta de destino:")
etiqueta_carpeta.pack()

carpeta_destino = tk.StringVar()
carpeta_destino.set("Seleccionar carpeta...")
etiqueta_ruta_carpeta = tk.Label(ventana, textvariable=carpeta_destino)
etiqueta_ruta_carpeta.pack()

boton_seleccionar_carpeta = tk.Button(ventana, text="Seleccionar carpeta", command=seleccionar_carpeta)
boton_seleccionar_carpeta.pack()

boton_descargar = tk.Button(ventana, text="Descargar", command=descargar_audio)
boton_descargar.pack()

ventana.mainloop()
