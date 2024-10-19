import tkinter as tk
from tkinter import messagebox
import os

def run_automation():
    os.chdir(r"C:\\Users\\bongi\\OneDrive\\Desktop\\dell")
    os.system("check")

    with open('check/xyz.txt', 'r') as file:
        content = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, content)

def about():
    messagebox.showinfo("About", "This is a simple automation GUI.")

root = tk.Tk()
root.title("Automation GUI")

# Set the background color or set a background image
background_image = tk.PhotoImage(file="background.png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=root.quit)

# Create a "Help" menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Create a button to run the automation
run_button = tk.Button(root, text="Run Automation", command=run_automation, bg="#59A96A")
run_button.pack(pady=20)

# Create a text widget to display the content of xyz.txt
text_widget = tk.Text(root, wrap="word", width=50, height=10, bg="#DFF7A7")
text_widget.pack(padx=10, pady=10)

root.mainloop()
