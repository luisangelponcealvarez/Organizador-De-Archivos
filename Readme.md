## File organizer by extension

This Python code uses the `tkinter` library to create a basic graphical interface that allows the user to select a destination folder. It then organizes the files in that folder into different subfolders according to their extension.

### Steps of the code:

~ Video on how to use the script

[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white)](https://youtu.be/5gdPYvYhZnk?si=QDVzT6dAJlueAwID)

~ Install python from: [Python downloads](https://www.python.org/downloads/)

~Clone this repository

```
git clone https://github.com/luisangelponcealvarez/OrganizadorDeArchivos.git
```

~ Import required libraries:

- `os`: For file system operations.

  ```
  pip install os
  ```

- `shutil`: To move files to destination folders.

  ```
  pip install shutil
  ```

- `tkinter`: To create a simple graphical interface.

  ```
  pip install tkinter
  ```

- `filedialog`: To display a folder selection dialog box.

  ```
  pip install filedialog
  ```

- `sys`: To handle program exit.
  ```
  pip install sys
  ```

This code is useful for organizing files in a user-selected folder by their extensions, making it easier to manage files in a cluttered directory.

### Steps to use the script

1. Run the script in a Python environment.

   ```
   py FileOrganizer.py
   ```

2. When running the script, a dialog box will prompt you to select the folder you want to organize.

3. Once the folder is selected, the script will proceed to organize the files into subfolders according to their extensions.

4. After organization is successfully completed, an info dialog box will be displayed indicating the files have been organized.

5. You can close the script after confirming the files have been organized.

![thumbnail](./thumbnail.png)
