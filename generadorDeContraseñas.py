import string
import random
import tkinter as tk

def generate_password():
    length = var.get()
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation.replace("'", "").replace('"', '').replace('\\', '').replace('/', '').replace('@', '')  # quitamos algunos caracteres especiales
    characters = lower + upper + digits + symbols
    password = ''.join(random.choice(characters) for i in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Configuración de la ventana principal
root = tk.Tk()
root.title('Generador de Contraseñas')

# Configuración de los widgets
length_label = tk.Label(root, text='Longitud:')
length_label.grid(row=0, column=0, padx=10, pady=10)

var = tk.IntVar(value=12)
length_entry = tk.Entry(root, textvariable=var, width=3)
length_entry.grid(row=0, column=1)

generate_button = tk.Button(root, text='Generar', command=generate_password)
generate_button.grid(row=0, column=2, padx=10)

password_label = tk.Label(root, text='Contraseña:')
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show='')
password_entry.grid(row=1, column=1, columnspan=2)

# Ejecución del programa
root.mainloop()