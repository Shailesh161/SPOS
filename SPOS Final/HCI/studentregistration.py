import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Function to handle the form submission
def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    contact = contact_entry.get()
    division = division_var.get()
    branch = branch_var.get()
    captcha = captcha_entry.get()

    # Validate the input
    if not all([name, age, email, phone, contact, division, branch, captcha]):
        messagebox.showerror("Error", "Please fill in all fields.")
    elif captcha != "OpenAI":
        messagebox.showerror("Captcha Error", "Please enter the correct CAPTCHA.")
    else:
        # You can save the student data to a file or a database here
        # For this example, we'll just display the data
        info_text = f"Name: {name}\nAge: {age}\nEmail: {email}\nPhone: {phone}\nContact: {contact}\nDivision: {division}\nBranch: {branch}"
        messagebox.showinfo("Registration Successful", info_text)

# Create the main window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("500x500")  # Set window size

# Create and place form elements
frame = ttk.Frame(root, padding=10, style="My.TFrame")
frame.grid(row=0, column=0, sticky="nsew")

style = ttk.Style()
style.configure("My.TFrame", background="white")

# Name
name_label = ttk.Label(frame, text="Name:", style="My.TLabel")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

name_entry = ttk.Entry(frame)
name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

# Age
age_label = ttk.Label(frame, text="Age:", style="My.TLabel")
age_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

age_entry = ttk.Entry(frame)
age_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

# Email
email_label = ttk.Label(frame, text="Email:", style="My.TLabel")
email_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

email_entry = ttk.Entry(frame)
email_entry.grid(row=2, column=1, padx=10, pady=5, sticky="w")

# Phone
phone_label = ttk.Label(frame, text="Phone:", style="My.TLabel")
phone_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")

phone_entry = ttk.Entry(frame)
phone_entry.grid(row=3, column=1, padx=10, pady=5, sticky="w")

# Contact
contact_label = ttk.Label(frame, text="Contact:", style="My.TLabel")
contact_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")

contact_entry = ttk.Entry(frame)
contact_entry.grid(row=4, column=1, padx=10, pady=5, sticky="w")

# Division
division_label = ttk.Label(frame, text="Division:", style="My.TLabel")
division_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")

division_var = tk.StringVar()
division_combobox = ttk.Combobox(frame, textvariable=division_var, values=["A", "B", "C"])
division_combobox.grid(row=5, column=1, padx=10, pady=5, sticky="w")

# Branch
branch_label = ttk.Label(frame, text="Branch:", style="My.TLabel")
branch_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")

branch_var = tk.StringVar()
branch_combobox = ttk.Combobox(frame, textvariable=branch_var, values=["Computer Science", "Electrical Engineering", "Mechanical Engineering"])
branch_combobox.grid(row=6, column=1, padx=10, pady=5, sticky="w")

# CAPTCHA
captcha_label = ttk.Label(frame, text="CAPTCHA (Enter 'OpenAI'):", style="My.TLabel")
captcha_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")

captcha_entry = ttk.Entry(frame)
captcha_entry.grid(row=7, column=1, padx=10, pady=5, sticky="w")

# Submit Button
submit_button = ttk.Button(frame, text="Submit", command=submit_form)
submit_button.grid(row=8, columnspan=2, pady=10)

# Create a label for displaying error messages
error_label = ttk.Label(frame, text="", style="Error.TLabel")
error_label.grid(row=9, column=0, columnspan=2, pady=10)

# Style settings for labels and error messages
style.configure("My.TLabel", font=("Arial", 12), background="white")
style.configure("Error.TLabel", font=("Arial", 12), background="white", foreground="red")

# Start the GUI event loop
root.mainloop()
