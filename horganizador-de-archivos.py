import os
import shutil


def organize_files(path):
    for file in os.listdir(path):
        if "extension":
            if not os.path.exists(os.path.join(path, "extension")):
                os.mkdir(os.path.join(path, "extension"))
                shutil.move(os.path.join(path, file),
                            os.path.join(path, "extension", file))


print("Archivos organizados con éxito.")
