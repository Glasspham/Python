import random
import string
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Tạo hàm vẽ hình tròn xung quanh nút 'i'
def draw_circle_around_i(canvas, x, y, radius):
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black", width=2)
    # Vẽ chữ 'i' bên trong hình tròn
    canvas.create_text(x, y, text="i", font=("Times New Roman", 20), fill="black")

# Chú thích và hướng dẫn chơi
def show_instructions():
    instruction_text = "Instructions:\n This is a game to practice typing with 10 fingers.\n Game mode 2 with time limit of 10 seconds.\n Every time you press check, the time will reset until you enter without time and the game will stop.\n The scoring rule is correct +10 wrong -10 and change to a new character after pressing check or enter. "
    messagebox.showinfo("Game Instructions", instruction_text)

# Chức năng chọn từ ngẫu nhiên
def choose_word():
    return ''.join(random.choices(string.ascii_letters, k=5))   # k là số lượng kí tên xuất hiện 1 lần

# Chức năng kiểm tra từ đã nhập và cập nhật điểm
def check_word(event=None):
    global score, time_left, highest_score, timer  # Include the 'timer' global variable

    if time_left > 0:
        entered_word = entry.get()
        current_word = display_label.cget("text")
        
        if entered_word == current_word:
            display_label.config(text=choose_word())
            result_label.config(text="Correct", fg="green")
            score += 10

            if score > highest_score:
                highest_score = score
                hscore_label.config(text=f"Highest point: {highest_score}")

            # After 2 seconds, reset the result_label
            root.after(2000, lambda: result_label.config(text=""))  

            # Reset the timer when the word entered is correct
            root.after_cancel(timer)
            time_left = 10
            update_time()
        else:
            display_label.config(text=choose_word())
            if entered_word == "":
                result_label.config(text="Please enter a word", fg="red")
            else:
                result_label.config(text="Incorrect, try again", fg="red")
                score -= 10
                time_left = 10  # Resetting the time if the word is incorrect
                root.after_cancel(timer)
                update_time()    

            # After 2 seconds, reset the result_label
            root.after(2000, lambda: result_label.config(text=""))  
            
        entry.delete(0, tk.END)
        score_label.config(text=f"Score: {score}")

# Chức năng thời gian
def update_time():
    global time_left, timer
    time_left -= 1
    time_label.config(text=f"Time Left: {time_left} seconds")

    if time_left == 0:
        root.after_cancel(timer)
        check_button.config(text="Time's up!", state=tk.DISABLED)
        # Stop the game when time runs out
    else:
        timer = root.after(1000, update_time)

# Chức năng reset game không cần run lại code
def reset_game():
    global score, time_left, timer
    score = 0
    time_left = 10
    score_label.config(text=f"Score: {score}")
    time_label.config(text=f"Time Left: {time_left} seconds")
    display_label.config(text=choose_word())
    result_label.config(text="")
    check_button.config(text="Kiểm tra", state=tk.NORMAL)
    root.after_cancel(timer)  # Reset the timer when the game is reset
    update_time()  # Start the timer again

root = tk.Tk()
root.title("Speed Typing")
score = 0
highest_score = 0  # Tạo biến để lưu điểm cao nhất
time_left = 10
image_path = ""  # Đặt đường dẫn tới hình ảnh của bạn. Còn không thì để trống 

# Xử lý ảnh
if image_path.strip() == "":
    # Nếu đường dẫn trống, tạo màu nền mặc định (màu xanh)
    window_width, window_height = 800, 500
    background_photo = tk.PhotoImage(width=window_width, height=window_height)
else:
    try:
        # Tải hình ảnh nếu có đường dẫn
        background_image = Image.open(image_path)
        window_width, window_height = 800, 500
        background_image = background_image.resize((window_width, window_height))
        background_photo = ImageTk.PhotoImage(background_image)
    except FileNotFoundError:
        # Nếu không tìm thấy tệp hình ảnh, sử dụng màu nền mặc định (màu xanh)
        window_width, window_height = 800, 500
        background_photo = tk.PhotoImage(width=window_width, height=window_height)

# Tạo Canvas để đặt ảnh nền
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#00FFFF") # Thay đổi màu bằng tên hoặc dùng mã màu HEX CODE
canvas.place(x=0, y=0, relwidth=1, relheight=1)

# Đặt ảnh nền vào Canvas ở phía dưới
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

# Tạo Canvas để vẽ hình tròn xung quanh chữ 'i'
info_canvas = tk.Canvas(root, width=30, height=30, highlightthickness=0)
info_canvas.place(x=760, y=10)

# Vẽ hình tròn xung quanh chữ 'i' trên Canvas
draw_circle_around_i(info_canvas, 15, 15, 13)

# Gắn hàm hiển thị hướng dẫn với sự kiện click vào hình tròn 'i'
info_canvas.bind("<Button-1>", lambda event: show_instructions())

# Các chức năng trong game
# Hiện chữ ngẫu nhiên
display_label = tk.Label(root, text=choose_word(), font=("Times New Roman", 40), justify='center')
display_label.pack(padx=20, pady=(80, 20), anchor='center')

# Ô người dùng nhập
entry = tk.Entry(root, width=30, font=("Times New Roman", 20))
entry.pack(padx=20, pady=10, anchor='center')
entry.bind("<Return>", check_word) 

# Nút kiểm tra
check_button = tk.Button(root, text="Check", command=check_word, font=("Times New Roman", 30))
check_button.pack(padx=20, pady=10, anchor='center')

# Hiện ra đúng hay sai
result_label = tk.Label(root, text="", font=("Times New Roman", 25)) # 
result_label.pack(padx=20, pady=10, anchor='center')

# Ô điểm
score_label = tk.Label(root, text=f"Score: {score}", font=("Times New Roman", 20))
score_label.pack(padx=20, pady=10, anchor='center')

# Ô thời gian
time_label = tk.Label(root, text=f"Time Left: {time_left} seconds", font=("Times New Roman", 20))
time_label.pack(padx=20, pady=10, anchor='center')

# Ký tên
name_label = tk.Label(root, text="Glasspham", font=("Times New Roman", 10))
name_label.place(x=10, y=10)

# Tạo Label để hiển thị điểm cao nhất
hscore_label = tk.Label(root, text=f"Highest point: {highest_score}", font=("Times New Roman", 20))
hscore_label.place(x=20, y=100)  # Đặt vị trí hiển thị của điểm cao nhất

# Tạo nút reset
play_again_button = tk.Button(root, text="Reset", command=reset_game, font=("Times New Roman", 20))
play_again_button.place(x=20, y=200)

# Begin the countdown
update_time()
root.geometry("800x500")
root.mainloop()