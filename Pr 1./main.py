import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

MORZE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    
    '.': '.-.-.-', ',': '--..--', ':': '---...',
    '?': '..--..', '-': '-....-', ')': '-.--.-',
    '/': '-..-.', '"': '-..-.', ';': '-.-.-.',
    '=': '-...-', '+': '.-.-.', '(': '-.--.', 
    ')': '-.--.-'
}

Morze_R = {value: key for key, value in MORZE.items()}

def text_to_morse(text):
    morse_text = " "
    for char in text:
        if char.upper() in MORZE:
            morse_text += MORZE[char.upper()] + " "
        else:
            morse_text += " "
    return morse_text

def from_morse(s):
    return ''.join(Morze_R.get(i) for i in s.split()).lower()

def input_from_keyboard():
    user_input = input_text.get("1.0", "end-1c")
    if user_input:
        morse_text = text_to_morse(user_input)
        messagebox.showinfo("Текст на азбуке Морзе", morse_text)
    else:
        messagebox.showwarning("Предупреждение", "Поле ввода пусто")

def input_from_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'r') as file:
            file_data = file.read()
            morse_text = text_to_morse(file_data)
            messagebox.showinfo("Текст на азбуке Морзе", morse_text)

root = tk.Tk()
root.title("Выбор ввода данных")

input_text = tk.Text(root, height=10, width=50)
input_text.pack()

button_keyboard = tk.Button(root, text="Ввести с клавиатуры", command=input_from_keyboard)
button_keyboard.pack()

button_file = tk.Button(root, text="Загрузить файл", command=input_from_file)
button_file.pack()

root.mainloop()
                  
