import os
import shutil
import tkinter as tk
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()

extensions = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Audios": [".mp3", ".WAV", ".AIFF", ".FLAC", ".AAC", ".OGG", ".WMA", ".DSD", ".ALAC", ".APE"],
    "Documentos": [".doc", ".docx", ".pdf", ".txt", ".rtf", ".odt", ".html", ".xml", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"],
}

for category, exts in extensions.items():
    category_path = os.path.join(file_path, category)
    os.makedirs(category_path, exist_ok=True)
    for file in os.listdir(file_path):
        if os.path.isfile(os.path.join(file_path, file)):
            if os.path.splitext(file)[-1].lower() in exts:
                shutil.move(
                    os.path.join(file_path, file),
                    os.path.join(category_path, file),
                )

tk.messagebox.showinfo(
    "Organización completada", "Los archivos han sido organizados correctamente."
)

# Salir del proceso después de que se complete la organización
sys.exit()
