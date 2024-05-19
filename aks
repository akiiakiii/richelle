import tkinter as tk
from tkinter import ttk
import math

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def delete():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def square_root():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def sine():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def cosine():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Mathematical Calculator ")
root.config(bg="orange")

font_style = ("Helvetica", 18, "bold")

basic_frame = ttk.Frame(root, padding="10")
basic_frame.grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(basic_frame, width=20, borderwidth=5, font=font_style)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons_basic = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "Del"
]

row = 1
col = 0
for button_text in buttons_basic:
    if button_text == "=":
        tk.Button(basic_frame, text=button_text, padx=20, pady=10, command=calculate, bg="red", fg="yellow",
                  font=font_style).grid(row=row, column=col)
    elif button_text == "C":
        tk.Button(basic_frame, text=button_text, padx=20, pady=10, command=clear, bg="gray", fg="red",
                  font=font_style).grid(row=row, column=col)
    elif button_text == "Del":
        tk.Button(basic_frame, text=button_text, padx=10, pady=10, command=delete, bg="gray", fg="black",
                  font=font_style).grid(row=row, column=col)
    elif button_text in ["âˆš", "sin", "cos", "xÂ²", "asin", "acos", "tan", "atan"]:
        if button_text == "âˆš":
            cmd = square_root
        elif button_text == "sin":
            cmd = sine
        elif button_text == "cos":
            cmd = cosine
        tk.Button(basic_frame, text=button_text, padx=15, pady=15, command=cmd, bg="gray", fg="white",
                  font=font_style).grid(row=row, column=col)
    else:
        tk.Button(basic_frame, text=button_text, padx=15, pady=15, command=lambda x=button_text: entry.insert(tk.END, x),
                  font=font_style).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1


extra_frame = ttk.Frame(root, padding="10")
extra_frame.grid(row=1, column=0, padx=5, pady=10)

ext_style = ("Helvetica", 10, "bold")

buttons_extra = [
    "xÂ³", "exp", "!", "log",
    "sin", "asin", "cos", "acos",
    "tan", "atan","âˆš", "xÂ²"
]

row = 0
col = 0
for button_text in buttons_extra:
    if button_text == "=":
        tk.Button(extra_frame, text=button_text, padx=20, pady=10, command=calculate, bg="red", fg="yellow",
                  font=ext_style).grid(row=row, column=col)
    elif button_text == "C":
        tk.Button(extra_frame, text=button_text, padx=20, pady=10, command=clear, bg="gray", fg="orange",
                  font=ext_style).grid(row=row, column=col)
    elif button_text == "Del":
        tk.Button(extra_frame, text=button_text, padx=10, pady=10, command=delete, bg="gray", fg="white",
                  font=ext_style).grid(row=row, column=col)
    elif button_text in ["âˆš", "sin", "cos", "xÂ²", "asin", "acos", "tan", "atan"]:
        if button_text == "âˆš":
            cmd = square_root
        elif button_text == "sin":
            cmd = sine
        elif button_text == "cos":
            cmd = cosine
        tk.Button(extra_frame, text=button_text, padx=20, pady=10, command=cmd, bg="white", fg="black",
                  font=ext_style).grid(row=row, column=col)
    else:
        tk.Button(extra_frame, text=button_text, padx=20, pady=10, command=lambda x=button_text: entry.insert(tk.END, x),
                  font=ext_style).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
