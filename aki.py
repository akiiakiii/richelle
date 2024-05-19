import tkinter as tk

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

root = tk.Tk()
root.title("my cal ")
root.config(bg="orange")
root.option_add("*Font", "Times 18")


entry = tk.Entry(root, width=18, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=20, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row = 1
col = 0
for button_text in buttons:
    if button_text == "=":
        tk.Button(root, text=button_text, padx=30, pady=20, command=calculate, bg = "red", fg="yellow", font=("Times New Roman", 18)).grid(row=row, column=col)
    elif button_text == "C":
        tk.Button(root, text=button_text, padx=30, pady=20, command=clear,
bg = "black", fg="orange", font=("Times New Roman", 18)).grid(row=row, column=col)
    else:
        tk.Button(root, text=button_text, padx=30, pady=20, command=lambda x=button_text: entry.insert(tk.END, x), font=("Times New Roman", 14)).grid(row=row, column=col)
    
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
