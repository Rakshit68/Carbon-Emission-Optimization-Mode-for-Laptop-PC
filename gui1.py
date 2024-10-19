import tkinter as tk
from tkinter import messagebox
import os

def run_automation():
    os.chdir(r"C:\Users\Rakshit\Desktop")
    os.system("check")
    #text_widget.insert(tk.END,"Apps recommended to close:")
    with open(r"C:\Users\Rakshit\Desktop\Recommendations.txt", 'r') as file:
        content = file.read()
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END,"Apps recommended to close:\n")
        text_widget.insert(tk.END, content)



def get_input():
    user_input = entry.get()
    return user_input

def new():
    root = tk.Tk()
    root.title("Input Example")

    # Create a Label to display instructions
    instruction_label = tk.Label(root, text="Enter Interval(in seconds):")
    instruction_label.pack(padx=10, pady=5)

    # Create an Entry widget to take user input
    entry = tk.Entry(root)
    entry.pack(padx=10, pady=5)

    # Create a Button to trigger input retrieval
    submit_button = tk.Button(root, text="Submit", command=get_input)
    submit_button.pack(padx=10, pady=10)

    # Create a Label to display the result
    result_label = tk.Label(root, text="")
    result_label.pack(padx=10, pady=5)







def n():
    os.chdir(r"C:\Users\Rakshit\Desktop")
    os.system("check")
    #text_widget.insert(tk.END,"Apps recommended to close:")
    with open(r"C:\Users\Rakshit\Desktop\system_info.txt", 'r') as file:
        content = file.read()
        root.title(content)

root = tk.Tk()
root.title("Automation GUI")

def on_button_click( emission_value):
        message=(emission_value)
        print(message)

def set_button(value):
     print(value)
normal_button = tk.Button(root, text="Normal Optimizer", command=lambda: on_button_click(0.6))
normal_button.pack(padx=10, pady=10)

ultra_button = tk.Button(root, text="Ultra Optimizer", command=lambda: on_button_click(0.3))
ultra_button.pack(padx=10, pady=10)

interval_button = tk.Button(root, text="Set Interval", command=new)
interval_button.pack(padx=10,pady=10)

# Set the background color to an environmentally friendly color
root.configure(bg="#B0E57C")

# Create a button to run the automation
run_button = tk.Button(root, text="Run Optimizer", command=run_automation, bg="#59A96A")
run_button.pack(pady=20)

# Create a text widget to display the content of xyz.txt
text_widget = tk.Text(root, wrap="word", width=50, height=10, bg="#DFF7A7")
text_widget.pack(padx=10, pady=10)


root.mainloop()
