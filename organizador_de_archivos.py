import os
import shutil

# Solicita al usuario la ruta de la carpeta que desea organizar
ruta = input("Introduce la ruta de la carpeta que deseas organizar: ")

# Crea una lista con todas las extensiones de archivo que deseas organizar
extensiones = {
    "Videos": [".mp4", ".avi", ".mkv", ".mov"],
    "Imagenes": [".jpg", ".jpeg", ".png", ".gif"],
    "Documentos": [".pdf", ".docx", ".txt"],
    "Archivos": [".zip", ".rar", ".exe"]
}

# Crea las carpetas para cada tipo de archivo si no existen ya
for carpeta in extensiones.keys():
    if not os.path.exists(os.path.join(ruta, carpeta)):
        os.makedirs(os.path.join(ruta, carpeta))

# Itera sobre cada archivo en la carpeta y organízalos según su extensión
for archivo in os.listdir(ruta):
    nombre_archivo, extension = os.path.splitext(archivo)
    extension = extension.lower()

    # Busca la carpeta correspondiente para la extensión del archivo y mueve el archivo allí
    for carpeta, extensiones_validas in extensiones.items():
        if extension in extensiones_validas:
            shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, carpeta, archivo))
            break
