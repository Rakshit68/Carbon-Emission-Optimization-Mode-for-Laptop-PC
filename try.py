import tkinter as tk
import os

def n():
    with open(r"C:\Users\Rakshit\Desktop\system_info.txt", 'r') as file:
        content = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, content)

root = tk.Tk()
root.title("System Info Viewer")

# Set the background color to an environmentally friendly color
root.configure(bg="#B0E57C")

# Create a button to display system info
show_info_button = tk.Button(root, text="Show System Info", command=n, bg="#59A96A")
show_info_button.pack(pady=20)

# Create a text widget to display the content
text_widget = tk.Text(root, wrap="word", width=50, height=10, bg="#DFF7A7")
text_widget.pack(padx=10, pady=10)

root.mainloop()