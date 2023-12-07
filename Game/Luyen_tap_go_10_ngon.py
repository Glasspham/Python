import random
import string
import tkinter as tk

# Lựa chọn từ điển pháp
def choose_word():
    return ''.join(random.choices(string.ascii_letters, k=5))

# Kiểm tra tính đúng đắn của từ nhập vào
def check_word(event=None):
    entered_word = entry.get()
    if entered_word == display_label.cget("text"):
        display_label.config(text=choose_word())
        result_label.config(text="Correct", fg="green")
        entry.delete(0, tk.END)
    else:
        result_label.config(text="InCorrect", fg="red")

root = tk.Tk()
root.title("Mô phỏng nhập liệu")

initial_word = choose_word()

display_label = tk.Label(root, text=initial_word, font=("Arial", 40), justify='center')
display_label.pack(padx=20, pady=(80, 20), anchor='center')

entry = tk.Entry(root, width=30, font=("Arial", 20))
entry.pack(padx=20, pady=10, anchor='center')
entry.bind("<Return>", check_word)  

check_button = tk.Button(root, text="Kiểm tra", command=check_word, font=("Arial", 30))
check_button.pack(padx=20, pady=10, anchor='center')

result_label = tk.Label(root, text="", font=("Arial", 25))
result_label.pack(padx=20, pady=10, anchor='center')

root.geometry("800x400")  # Thiết lập kích thước cửa sổ 

root.mainloop()
