import random
import string
import tkinter as tk

# Lựa chọn từ điển pháp
def choose_word():
    return ''.join(random.choices(string.ascii_letters, k=5))

# Kiểm tra tính đúng đắn của từ nhập vào và tính điểm
def check_word(event=None):
    global score, time_left
    if time_left > 0:
        entered_word = entry.get()
        current_word = display_label.cget("text")
        
        if entered_word == current_word:
            display_label.config(text=choose_word())
            result_label.config(text="Correct", fg="green")
            score += 1
        else:
            if entered_word == "":
                result_label.config(text="Please enter a word", fg="red")
            else:
                result_label.config(text="Incorrect, try again", fg="red")

        entry.delete(0, tk.END)
        score_label.config(text=f"Score: {score}")
    else:
        result_label.config(text="Time's up!", fg="blue")
        check_button.config(text="Time's up!", state=tk.DISABLED)  # Vô hiệu hóa nút Kiểm tra khi hết thời gian

# Cập nhật thời gian và kiểm tra khi hết thời gian
def update_time():
    global time_left, timer
    time_left -= 1
    time_label.config(text=f"Time Left: {time_left} seconds")

    if time_left == 0:
        root.after_cancel(timer)
        check_button.config(text="Time's up!", state=tk.DISABLED)  # Vô hiệu hóa nút Kiểm tra khi hết thời gian
    else:
        timer = root.after(1000, update_time)

root = tk.Tk()
root.title("Mô phỏng nhập liệu")

score = 0  # Điểm ban đầu
time_left = 10  # Thời gian chơi ban đầu (10 giây)

display_label = tk.Label(root, text=choose_word(), font=("Open Sans", 40), justify='center')
display_label.pack(padx=20, pady=(80, 20), anchor='center')

entry = tk.Entry(root, width=30, font=("Open Sans", 20))
entry.pack(padx=20, pady=10, anchor='center')
entry.bind("<Return>", check_word)  

check_button = tk.Button(root, text="Kiểm tra", command=check_word, font=("Open Sans", 30))
check_button.pack(padx=20, pady=10, anchor='center')

result_label = tk.Label(root, text="", font=("Open Sans", 25))
result_label.pack(padx=20, pady=10, anchor='center')

score_label = tk.Label(root, text=f"Score: {score}", font=("Open Sans", 20))
score_label.pack(padx=20, pady=10, anchor='center')

time_label = tk.Label(root, text=f"Time Left: {time_left} seconds", font=("Open Sans", 20))
time_label.pack(padx=20, pady=10, anchor='center')

# Bắt đầu đếm thời gian
update_time()

root.geometry("800x500")  # Thiết lập kích thước cửa sổ là 800x500

root.mainloop()
