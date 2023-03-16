from PIL import Image 
import os 
rutaActual = os.path.dirname(os.path.abspath(__file__))

def formatRuta(ruta):
  clean = ""
  for caracter in ruta:
    if caracter == "\\":
      clean = clean + "/"
    else:
      clean = clean + caracter
  return clean

descargasFolder = formatRuta(rutaActual) + "/"

organized_files = descargasFolder + "/ArchivosOrganizados"
organized_filesImages = descargasFolder + "/ArchivosOrganizados/imgDescargadas"
organized_filesVideos = descargasFolder + "/ArchivosOrganizados/videosDescargados"
organized_filesRar = descargasFolder + "/ArchivosOrganizados/RarDescargadas"
organized_filesExe = descargasFolder + "/ArchivosOrganizados/ExeDescargadas"

os.mkdir(organized_files)
os.mkdir(organized_filesImg)
os.mkdir(organized_filesVideos)
os.mkdir(organized_filesRar)
os.mkdir(organized_filesExe)

if __nam__ = "__main__":
  
  for filename in os.listdir(downloadsFolder):
    name.extension = os.path.splitext(downloadsFolder + filename)
    picture = Image.open(downloadsFolder + filename)
    picture.save(organized_filesImg + "/" + "compressed_" + filename, optimized=true, quality=60)
    os.remove(downloadsFolder + filename)

