"""
Smart Password Generator
-------------------------
A simple Tkinter-based GUI application that generates strong passwords
from a user-supplied word or fully at random, and checks password strength.

Author: Anjali Patange
"""

import random
import string
import tkinter as tk
from tkinter import messagebox


# -------- Password Strength Function --------
def check_strength(password):
    length = len(password)
    upper = any(c.isupper() for c in password)
    lower = any(c.islower() for c in password)
    digit = any(c.isdigit() for c in password)
    symbol = any(c in "!@#$%^&*" for c in password)

    score = 0
    if length >= 8:
        score += 1
    if upper:
        score += 1
    if lower:
        score += 1
    if digit:
        score += 1
    if symbol:
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"


# -------- Generate Password (word-based) --------
def generate_password():
    user = entry_word.get()
    if user == "":
        messagebox.showwarning("Input Error", "Please enter a word")
        return

    password = (
        user.replace('a', '@')
        .replace('s', '$')
        .replace('o', '0')
        .replace('i', '1')
    )
    number = str(random.randint(0, 9))
    symbol = random.choice("!@#$%&*")
    final_password = password + number + symbol

    entry_result.delete(0, tk.END)
    entry_result.insert(0, final_password)

    # strength
    strength = check_strength(final_password)
    label_strength.config(text="Strength: " + strength)

    # color
    if strength == "Weak":
        label_strength.config(fg="red")
    elif strength == "Medium":
        label_strength.config(fg="orange")
    else:
        label_strength.config(fg="green")


# -------- Random Strong Password --------
def random_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    pwd = ''.join(random.choice(chars) for _ in range(12))

    entry_result.delete(0, tk.END)
    entry_result.insert(0, pwd)

    strength = check_strength(pwd)
    label_strength.config(text="Strength: " + strength, fg="green")


# -------- Copy to Clipboard --------
def copy_password():
    pwd = entry_result.get()
    root.clipboard_clear()
    root.clipboard_append(pwd)
    messagebox.showinfo("Copied", "Password copied to clipboard!")


# -------- Clear Fields --------
def clear_all():
    entry_word.delete(0, tk.END)
    entry_result.delete(0, tk.END)
    label_strength.config(text="Strength: ")


# -------- GUI Window --------
root = tk.Tk()
root.title("Smart Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Title
tk.Label(root, text="Password Generator", font=("Arial", 16, "bold")).pack(pady=10)

# Input
tk.Label(root, text="Enter Word:").pack()
entry_word = tk.Entry(root, width=30)
entry_word.pack(pady=5)

# Generate button
tk.Button(
    root, text="Generate Password", command=generate_password, bg="lightblue"
).pack(pady=8)

# Random button
tk.Button(
    root, text="Random Strong Password", command=random_password, bg="lightgreen"
).pack(pady=5)

# Result
tk.Label(root, text="Generated Password:").pack()
entry_result = tk.Entry(root, width=30)
entry_result.pack(pady=5)

# Strength label
label_strength = tk.Label(root, text="Strength: ", font=("Arial", 12, "bold"))
label_strength.pack(pady=5)

# Buttons
tk.Button(root, text="Copy Password", command=copy_password).pack(pady=5)
tk.Button(root, text="Clear", command=clear_all).pack(pady=5)

root.mainloop()
