import tkinter as tk
from tkinter import messagebox
import random

# Function to check the login credentials
def login():
    username = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    address = address_entry.get()
    captcha = captcha_entry.get()

    # Check if the captcha is correct
    if captcha == str(captcha_value):
        messagebox.showinfo("Login", "Login Successful!\nName: {}\nPhone: {}\nEmail: {}\nAddress: {}".format(username, phone, email, address))
    else:
        messagebox.showerror("Login Error", "Incorrect Captcha!")

# Function to generate a random 4-digit captcha
def generate_captcha():
    global captcha_value
    captcha_value = random.randint(1000, 9999)
    captcha_label.config(text=str(captcha_value))

# Create the main window
root = tk.Tk()
root.title("Login Form")
root.geometry("600x500")  # Set the window size

# Set a background color for the root window
root.configure(bg="#3498db")  # Blue background color

# Create a frame to enclose the form and add a square outline
frame = tk.Frame(root, borderwidth=2, relief="solid")
frame.pack(padx=25, pady=25, fill=tk.BOTH, expand=True)

# Create labels and entry widgets with increased font size and width
name_label = tk.Label(frame, text="Name:", font=("Arial", 20))
name_label.pack()
name_entry = tk.Entry(frame, font=("Arial", 20), width=35)  # Increased width
name_entry.pack()

phone_label = tk.Label(frame, text="Phone:", font=("Arial", ))
phone_label.pack()
phone_entry = tk.Entry(frame, font=("Arial", 20), width=35)  # Increased width
phone_entry.pack()

email_label = tk.Label(frame, text="Email:", font=("Arial", 20))
email_label.pack()
email_entry = tk.Entry(frame, font=("Arial", 20), width=35)  # Increased width
email_entry.pack()

password_label = tk.Label(frame, text="Password:", font=("Arial", 20))
password_label.pack()
password_entry = tk.Entry(frame, font=("Arial", 20), show="*", width=35)  # Increased width
password_entry.pack()

address_label = tk.Label(frame, text="Address:", font=("Arial", 20))
address_label.pack()
address_entry = tk.Entry(frame, font=("Arial", 20), width=35)  # Increased width
address_entry.pack()

captcha_label = tk.Label(frame, text="Captcha:", font=("Arial", 20))
captcha_label.pack()
generate_captcha()  # Generate the initial captcha
captcha_entry = tk.Entry(frame, font=("Arial", 20), width=35)  # Increased width
captcha_entry.pack()

# Create a button for login with a background color
login_button = tk.Button(frame, text="Login", command=login, font=("Arial", 20), bg="#e74c3c")  # Red background color
login_button.pack()

# Create a button to generate a new captcha with a background color
new_captcha_button = tk.Button(frame, text="New Captcha", command=generate_captcha, font=("Arial", 20), bg="#2ecc71")  # Green background color
new_captcha_button.pack()

# Start the Tkinter main loop
root.mainloop()
