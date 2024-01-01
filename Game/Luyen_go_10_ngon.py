import random
import string
import tkinter as tk
from PIL import Image, ImageTk

# Chức năng chọn từ ngẫu nhiên
def choose_word():
    return ''.join(random.choices(string.ascii_letters, k=5))   # k là số lượng kí tên xuất hiện 1 lần

# Chức năng kiểm tra từ đã nhập và cập nhật điểm
def check_word(event=None):
    global score, time_left, highest_score  # Bao gồm highest_score là biến toàn cục
    if time_left > 0:
        entered_word = entry.get()
        current_word = display_label.cget("text")
        
        if entered_word == current_word:
            display_label.config(text=choose_word())
            result_label.config(text="Correct", fg="green")
            score += 10             #Nhập đúng điểm +10

            if score > highest_score:
                highest_score = score  # Cập nhật highest_score nếu đạt được điểm cao mới
                hscore_label.config(text=f"Điểm cao nhất: {highest_score}")
                
        else:
            if entered_word == "":
                result_label.config(text="Please enter a word", fg="red")
            else:
                result_label.config(text="Incorrect, try again", fg="red")
                score -= 10                     

        entry.delete(0, tk.END)
        score_label.config(text=f"Score: {score}")

def update_time():
    global time_left, timer
    time_left -= 1
    time_label.config(text=f"Time Left: {time_left} seconds")

    if time_left == 0:
        root.after_cancel(timer)
        check_button.config(text="Time's up!", state=tk.DISABLED)
    else:
        timer = root.after(1000, update_time)

def reset_game(): # Reset game
    global score, time_left
    score = 0
    time_left = 25
    score_label.config(text=f"Score: {score}")
    time_label.config(text=f"Time Left: {time_left} seconds")
    display_label.config(text=choose_word())
    result_label.config(text="")
    check_button.config(text="Kiểm tra", state=tk.NORMAL)
    update_time()

root = tk.Tk()
root.title("Speed Typing")
score = 0
highest_score = 0  # Tạo biến để lưu điểm cao nhất
time_left = 25

# Load the image
background_image = Image.open ("path\Back.jpg")  # Thay thế bằng đường dẫn file ảnh của bạn
window_width, window_height = 800, 500
background_image = background_image.resize((window_width, window_height))
background_photo = ImageTk.PhotoImage(background_image)

# Tạo Canvas để đặt ảnh nền
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Đặt ảnh nền vào Canvas ở phía dưới
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Các vật dụng khác
display_label = tk.Label(root, text=choose_word(), font=("Times New Roman", 40), justify='center')
display_label.pack(padx=20, pady=(80, 20), anchor='center')

entry = tk.Entry(root, width=30, font=("Open Sans", 20))
entry.pack(padx=20, pady=10, anchor='center')
entry.bind("<Return>", check_word) 

check_button = tk.Button(root, text="Check", command=check_word, font=("Open Sans", 30))
check_button.pack(padx=20, pady=10, anchor='center')

# Thêm nút "Chơi lại" và gán chức năng reset_game cho nó
play_again_button = tk.Button(root, text="Reset", command=reset_game, font=("Open Sans", 20))
play_again_button.pack(padx=20, pady=10, anchor='center') 

result_label = tk.Label(root, text="", font=("Open Sans", 25)) # 

score_label = tk.Label(root, text=f"Score: {score}", font=("Open Sans", 20))
score_label.pack(padx=20, pady=10, anchor='center')

time_label = tk.Label(root, text=f"Time Left: {time_left} seconds", font=("Open Sans", 20))
time_label.pack(padx=20, pady=10, anchor='center')

name_label = tk.Label(root, text="Glasspham", font=("Open Sans", 10))
name_label.place(x=10, y=10)

# Tạo Label để hiển thị điểm cao nhất
hscore_label = tk.Label(root, text=f"Điểm cao nhất: {highest_score}", font=("Open Sans", 20))
hscore_label.place(x=20, y=100)  # Đặt vị trí hiển thị của điểm cao nhất

# Begin the countdown
update_time()

root.geometry("800x500")
root.mainloop()
