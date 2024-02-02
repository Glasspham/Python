import tkinter as tk
from tkinter import ttk, scrolledtext

def deCript(message, key):
    deCodedText = ''
    for char in message:
        if char.isalpha():
            case_offset = ord('A') if char.isupper() else ord('a')
            position = (ord(char) - key - case_offset) % totalPositions
            deCodedText += chr(position + case_offset)
        else:
            deCodedText += char
    return deCodedText

def enCript(message, key):
    codedText = ''
    for char in message:
        if char.isalpha():
            case_offset = ord('A') if char.isupper() else ord('a')
            position = (ord(char) + key - case_offset) % totalPositions
            codedText += chr(position + case_offset)
        else:
            codedText += char
    return codedText

def on_button_click():
    user_choice = choice_var.get()
    message = message_text.get("1.0", tk.END).strip()
    key = int(key_entry.get())

    if user_choice == 'Decrypt':
        result_text.set(f'Original message:\n{deCript(message, key)}')
    elif user_choice == 'Encrypt':
        result_text.set(f'Coded message:\n{enCript(message, key)}')

def copy_result():
    result = result_text.get()
    if 'Coded message' in result:
        result = result.split('Coded message:')[1].strip()
    root.clipboard_clear()
    root.clipboard_append(result)
    root.update()

# Initializare
plain = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalPositions = len(plain)

# Creare interfață grafică
root = tk.Tk()
root.title('Encrypt/Decrypt Tool by Glass')

# Elemente de interfată
choice_var = tk.StringVar()
choice_label =ttk.Label(root, text='Choose action: ')
choice_combobox = ttk.Combobox(root, textvariable=choice_var, values=['Encrypt', 'Decrypt'])
choice_combobox.set('Encrypt')

message_label =ttk.Label(root, text='Enter message: ')
message_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=30, height=5)
key_label =ttk.Label(root, text='Enter numeric key:')
key_entry = ttk.Entry(root, width=10)

result_text = tk.StringVar()
result_label = ttk.Label(root, textvariable=result_text)

execute_button = ttk.Button(root, text='Execute', command=on_button_click)
copy_button = ttk.Button(root, text='Copy Result', command=copy_result)

# Aranjare elemente in grid
choice_label.grid(row=0, column=0, padx=10, pady=10)
choice_combobox.grid(row=0, column=1, padx=10, pady=10)
message_label.grid(row=1, column=0, padx=10, pady=10)
message_text.grid(row=1, column=1, padx=10, pady=10)
key_label.grid(row=2, column=0, padx=10, pady=10)
key_entry.grid(row=2, column=1, padx=10, pady=10)
execute_button.grid(row=3, column=0, pady=10)
copy_button.grid(row=3, column=1, pady=10)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Ruleazā aplicația
root.mainloop()