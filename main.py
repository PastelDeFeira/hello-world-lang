import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import time

# Global variable to store file path
file_path = None

def show_about():
    messagebox.showinfo("About", "Hello World Lang is a joke programming language made by PastelDeFeira (with heavy collaboration from ChatGPT) where whatever you input outputs 'Hello World!'")

def new_file():
    global file_path
    file_path = None
    text_area.delete("1.0", "end")
    root.title("Untitled - Hello World Lang")

def open_file():
    global file_path
    file_path = filedialog.askopenfilename(defaultextension=".helloworld", filetypes=[("Hello World Files", "*.helloworld"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as f:
            text_area.delete("1.0", "end")
            text_area.insert("1.0", f.read())
        root.title(f"{file_path.split('/')[-1]} - Hello World Lang")

def save_file():
    global file_path
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_area.get("1.0", "end-1c"))
        root.title(f"{file_path.split('/')[-1]} - Hello World Lang")
    else:
        save_file_as()

def save_file_as():
    global file_path
    file_path = filedialog.asksaveasfilename(defaultextension=".helloworld", filetypes=[("Hello World Files", "*.helloworld"), ("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(text_area.get("1.0", "end-1c"))
        root.title(f"{file_path.split('/')[-1]} - Hello World Lang")

def compile_now():
    code = text_area.get("1.0", "end-1c")
    if not code:
        messagebox.showwarning("Warning", "Cannot compile empty program!")
        return
    progress_bar = tk.ttk.Progressbar(root, mode='indeterminate')
    progress_bar.pack(side=tk.BOTTOM, fill=tk.X)
    progress_bar.start(10 * len(code))
    root.after(10 * len(code), lambda: progress_bar.pack_forget())
    root.after(10 * len(code), lambda: print("Hello World!"))



root = tk.Tk()
root.title("Hello World Compiler")
root.geometry("900x600")

# Create menu bar
menu_bar = tk.Menu(root)

# Create file menu and add options
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", state="disabled", command=save_file)
file_menu.add_command(label="Save As", command=save_file_as)
menu_bar.add_cascade(label="File", menu=file_menu)

# Create compile menu and add options
compile_menu = tk.Menu(menu_bar, tearoff=0)
compile_menu.add_command(label="Compile Now", command=compile_now)
menu_bar.add_cascade(label="Compile", menu=compile_menu)

# Create about menu and add option
about_menu = tk.Menu(menu_bar, tearoff=0)
about_menu.add_command(label="About", command=show_about)
menu_bar.add_cascade(label="About", menu=about_menu)

# Add menu bar to window
root.config(menu=menu_bar)

# Create text area
text_area = tk.Text(root, bg="white", fg="black", insertbackground="black")
text_area.pack(expand=True, fill="both")

root.mainloop()
