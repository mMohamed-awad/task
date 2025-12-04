import tkinter as tk

def add(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get().replace("^", "**")
        entry.delete(0, tk.END)
        entry.insert(0, eval(expression))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Row 1
tk.Button(root, text="7", width=5, height=2, command=lambda: add("7")).grid(row=1, column=0)
tk.Button(root, text="8", width=5, height=2, command=lambda: add("8")).grid(row=1, column=1)
tk.Button(root, text="9", width=5, height=2, command=lambda: add("9")).grid(row=1, column=2)
tk.Button(root, text="/", width=5, height=2, command=lambda: add("/")).grid(row=1, column=3)

# Row 2
tk.Button(root, text="4", width=5, height=2, command=lambda: add("4")).grid(row=2, column=0)
tk.Button(root, text="5", width=5, height=2, command=lambda: add("5")).grid(row=2, column=1)
tk.Button(root, text="6", width=5, height=2, command=lambda: add("6")).grid(row=2, column=2)
tk.Button(root, text="*", width=5, height=2, command=lambda: add("*")).grid(row=2, column=3)

# Row 3
tk.Button(root, text="1", width=5, height=2, command=lambda: add("1")).grid(row=3, column=0)
tk.Button(root, text="2", width=5, height=2, command=lambda: add("2")).grid(row=3, column=1)
tk.Button(root, text="3", width=5, height=2, command=lambda: add("3")).grid(row=3, column=2)
tk.Button(root, text="-", width=5, height=2, command=lambda: add("-")).grid(row=3, column=3)

# Row 4
tk.Button(root, text="0", width=5, height=2, command=lambda: add("0")).grid(row=4, column=0)
tk.Button(root, text="%", width=5, height=2, command=lambda: add("%")).grid(row=4, column=1)
tk.Button(root, text="^", width=5, height=2, command=lambda: add("^")).grid(row=4, column=2)
tk.Button(root, text="+", width=5, height=2, command=lambda: add("+")).grid(row=4, column=3)

# Row 5
tk.Button(root, text="C", width=5, height=2, command=clear).grid(row=5, column=0)
tk.Button(root, text="=", width=17, height=2, command=calculate).grid(row=5, column=1, columnspan=3)

root.mainloop()
