import random
import string
import tkinter as tk


def generate_password():
    password_length = int(length_input.get())
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars)
                       for i in range(password_length))
    password_output.delete(0, tk.END)
    password_output.insert(0, password)


# Crea la ventana principal
root = tk.Tk()
root.geometry("600x600")
root.title("Generador de contraseñas")

# Crea una etiqueta y un campo de entrada para la longitud de la contraseña
length_label = tk.Label(root, text="Longitud de la contraseña:")
length_label.pack()
length_input = tk.Entry(root)
length_input.pack()

# Crea un botón para generar una contraseña aleatoria
generate_button = tk.Button(
    root, text="Generar contraseña", command=generate_password)
generate_button.pack()

# Crea una etiqueta y un campo de texto para mostrar la contraseña generada
password_label = tk.Label(root, text="Contraseña generada:")
password_label.pack()
password_output = tk.Entry(root)
password_output.pack()

# Inicia el loop principal de la aplicación
root.mainloop()
