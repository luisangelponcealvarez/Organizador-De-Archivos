import tkinter as tk
import random
import string

def generate_password():
    # Define the length of the password
    password_length = 20
    
    # Define the characters to be used in the password
    password_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(password_characters) for i in range(password_length))
    
    # Update the label with the generated password
    password_label.configure(text="Generated Password: " + password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")

# Create the label to display the generated password
password_label = tk.Label(window, text="Click 'Generate Password' to create a new password!")
password_label.pack()

# Create the button to generate a new password
generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack()

# Run the main loop
window.mainloop()
