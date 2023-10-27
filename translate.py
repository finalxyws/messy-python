# Import the necessary libraries
from googletrans import Translator
import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Translator")

# Create the input box
input_label = tk.Label(root, text="Enter the text you want to translate:")
input_label.pack()
input_box = tk.Entry(root)
input_box.pack()

# Create the output box
output_label = tk.Label(root, text="Translated text:")
output_label.pack()
output_box = tk.Entry(root)
output_box.pack()

# Function to translate the text
def translate_text():
    # Get the text from the input box
    text = input_box.get()

    # Get the language from the dropdown menu
    destination_language = destination_var.get()

    # Use the Googletrans library to translate the text to the desired language
    translator = Translator(service_urls='translate.google.cn')
    translated_text = translator.translate(text, dest=destination_language)

    # Set the translated text in the output box
    output_box.delete(0, tk.END)
    output_box.insert(0, translated_text.text)

# Create the button to translate the text
translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack()

# Create the dropdown menu for the destination language
destination_label = tk.Label(root, text="Select the language you want to translate to:")
destination_label.pack()
destination_var = tk.StringVar()
destination_box = ttk.Combobox(root, textvariable=destination_var, values=["English", "Chinese", "Spanish", "Japanese"])
destination_box.pack()

# Run the main loop
root.mainloop()
