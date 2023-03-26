import tkinter as tk
import random
import string

# Define the GUI window
window = tk.Tk()
window.title("Password Generator")

# Define the password generation function
def generate_password():
    length = int(length_entry.get())
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation
    all_chars = lowercase + uppercase + digits + punctuation
    password = ''.join(random.sample(all_chars, length))
    password_display.config(state=tk.NORMAL)
    password_display.delete(0, tk.END)
    password_display.insert(0, password)
    password_display.config(state=tk.DISABLED)

# Define the GUI elements
length_label = tk.Label(window, text="Password length:")
length_entry = tk.Entry(window, width=10)
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
password_display = tk.Entry(window, width=30, state=tk.DISABLED)

# Place the GUI elements in the window
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
password_display.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Set the window size
window.geometry("400x400")

# Start the GUI event loop
window.mainloop()
