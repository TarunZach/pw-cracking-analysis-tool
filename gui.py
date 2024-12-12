import tkinter as tk
from tkinter import messagebox
from analysis import analyze_password
from utils import generate_strong_password


def check_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return

    is_strong, message = analyze_password(password)
    if is_strong:
        result_label.config(text=message, fg="green")
    else:
        result_label.config(text=message, fg="red")
        stronger_password = generate_strong_password()
        suggestion_label.config(text=f"Suggested Strong Password: {stronger_password}")


root = tk.Tk()
root.title("Password Strength Analysis Tool")
root.geometry("400x300")

tk.Label(root, text="Enter Your Password:").pack(pady=10)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

analyze_button = tk.Button(root, text="Analyze Password", command=check_password)
analyze_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=350)
result_label.pack(pady=10)

suggestion_label = tk.Label(root, text="", fg="blue", wraplength=350)
suggestion_label.pack(pady=10)

root.mainloop()
