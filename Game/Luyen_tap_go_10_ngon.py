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

display_label = tk.Label(root, text=initial_word, font=("Arial", 18))
display_label.pack(padx=10, pady=10)

entry = tk.Entry(root, width=30)
entry.pack(padx=10, pady=10)
entry.bind("<Return>", check_word)  # Gán sự kiện nhấn phím Enter cho hành động kiểm tra

check_button = tk.Button(root, text="Kiểm tra", command=check_word)
check_button.pack(padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(padx=10, pady=10)

root.mainloop()
