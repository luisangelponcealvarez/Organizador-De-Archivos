## Organizador de archivos por extensión

Este código en Python utiliza la biblioteca `tkinter` para crear una interfaz gráfica básica que permite al usuario seleccionar una carpeta de destino. Luego, organiza los archivos en esa carpeta en diferentes subcarpetas según su extensión.

### Pasos del código:

~Clone this repository

```
git clone https://github.com/luisangelponcealvarez/OrganizadorDeArchivos.git
```

~Instala python desde: [Python downloads](https://www.python.org/downloads/)

~ Importación de las bibliotecas necesarias:

- `os`: Para operaciones de sistema de archivos.

  ```
  pip install os
  ```

- `shutil`: Para mover los archivos a las carpetas de destino.

  ```
  pip install shutil
  ```

- `tkinter`: Para crear una interfaz gráfica simple.

  ```
  pip install tkinter
  ```

- `filedialog`: Para mostrar un cuadro de diálogo de selección de carpeta.

  ```
  pip install filedialog
  ```

- `sys`: Para gestionar la salida del programa.
  ```
  pip install sys
  ```

Este código es útil para organizar archivos en una carpeta seleccionada por el usuario según sus extensiones, lo que facilita la gestión de archivos en un directorio desordenado.

### Pasos para usar el script

1. Ejecute el script en un entorno Python.

   ```
   py OrganizadorDeArchivos.py
   ```

2. Al ejecutar el script, aparecerá una ventana de diálogo que le pedirá que seleccione la carpeta que desea organizar.

3. Una vez seleccionada la carpeta, el script procederá a organizar los archivos en subcarpetas según sus extensiones.

4. Después de que la organización se complete con éxito, se mostrará un cuadro de diálogo de información indicando que los archivos se han organizado correctamente.

5. Puede cerrar el script después de confirmar que los archivos han sido organizados.

![miniatura](./miniatura.png)
