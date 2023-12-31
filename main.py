import os
import shutil
from tkinter import Tk, Label, Button, filedialog, Checkbutton, StringVar


class FileOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Organizador de Archivos")

        self.selected_folder = ""
        self.file_types = {
            "Imágenes": [".jpg", ".jpeg", ".png", ".gif"],
            "Videos": [".mp4", ".avi", ".mkv"],
            "Audios": [".mp3", ".wav", ".ogg"],
            "Documentos": [".doc", ".docx", ".pdf", ".txt"],
        }

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="Seleccionar Carpeta:").grid(row=0, column=0, pady=10)
        Button(self.root, text="Seleccionar", command=self.select_folder).grid(
            row=0, column=1, pady=10
        )

        Label(self.root, text="Tipos de Archivos:").grid(row=1, column=0, pady=10)
        self.checkbox_vars = {file_type: StringVar() for file_type in self.file_types}
        for i, (file_type, extensions) in enumerate(self.file_types.items(), start=2):
            Checkbutton(
                self.root, text=file_type, variable=self.checkbox_vars[file_type]
            ).grid(row=i, column=0, columnspan=2, sticky="w")

        Button(self.root, text="Organizar Archivos", command=self.organize_files).grid(
            row=i + 1, column=0, columnspan=2, pady=10
        )

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory()
        print("Carpeta Seleccionada:", self.selected_folder)

    def organize_files(self):
        if not self.selected_folder:
            print("Selecciona una carpeta primero.")
            return

        selected_types = [
            file_type
            for file_type, var in self.checkbox_vars.items()
            if var.get() == "1"
        ]
        if not selected_types:
            print("Selecciona al menos un tipo de archivo.")
            return

        for file_type in selected_types:
            destination_folder = os.path.join(self.selected_folder, file_type)
            os.makedirs(destination_folder, exist_ok=True)

            for file_name in os.listdir(self.selected_folder):
                file_path = os.path.join(self.selected_folder, file_name)
                if os.path.isfile(file_path) and any(
                    file_name.lower().endswith(ext)
                    for ext in self.file_types[file_type]
                ):
                    shutil.move(file_path, os.path.join(destination_folder, file_name))

        print("Archivos organizados.")


if __name__ == "__main__":
    root = Tk()
    app = FileOrganizer(root)
    root.mainloop()
