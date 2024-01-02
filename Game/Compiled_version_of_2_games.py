import random
import string
import tkinter as tk
from PIL import Image, ImageTk

# Tạo biến cho chế độ trò chơi
game_mode = 1  # Đặt chế độ trò chơi mặc định

# Chức năng chọn từ ngẫu nhiên
def choose_word():
    return ''.join(random.choices(string.ascii_letters, k=5))   # k là số lượng kí tên xuất hiện 1 lần

# Chức năng kiểm tra từ đã nhập và cập nhật điểm
def check_word_game1(event=None):
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
                hscore_label.config(text=f"Highest point: {highest_score}")
                
        else:
            display_label.config(text=choose_word())
            if entered_word == "":
                result_label.config(text="Please enter a word", fg="red")
            else:
                result_label.config(text="Incorrect, try again", fg="red")
                score -= 10                     

        entry.delete(0, tk.END)
        score_label.config(text=f"Score: {score}")

# Chức năng kiểm tra từ đã nhập và cập nhật điểm
def check_word_game2(event=None):
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

        entry.delete(0, tk.END)
        score_label.config(text=f"Score: {score}")

# Hàm check_word tổng quát phản ánh cả hai trò chơi
def check_word(event=None):
    global game_mode
    if game_mode == 1:
        check_word_game1()  # Gọi hàm xử lý cho Game 1
    else:
        check_word_game2() 
# Chức năng thời gian

def update_time():
    global time_left, timer
    time_left -= 1
    time_label.config(text=f"Time Left: {time_left} seconds")

    if time_left == 0:
        root.after_cancel(timer)
        check_button.config(text="Time's up!", state=tk.DISABLED)
    else:
        timer = root.after(1000, update_time)
       
def reset_game():
    global score, time_left, game_mode
    score = 0
    if game_mode == 1:
        time_left = 25  # Thời gian cho chế độ Game 1
    elif game_mode == 2:
        time_left = 10  # Thời gian cho chế độ Game 2
    score_label.config(text=f"Score: {score}")
    time_label.config(text=f"Time Left: {time_left} seconds")
    display_label.config(text=choose_word())
    result_label.config(text="")
    check_button.config(text="Check", state=tk.NORMAL)
    update_time()

def change_game_mode(mode):
    global game_mode, time_left
    game_mode = mode
    if game_mode == 1:
        time_left = 25  # Thời gian cho chế độ Game 1
    elif game_mode == 2:
        time_left = 10  # Thời gian cho chế độ Game 2
    time_label.config(text=f"Time Left: {time_left} seconds")  # Cập nhật label hiển thị thời gian
    root.after_cancel(timer)  # Hủy timer hiện tại
    update_time()  # Gọi lại hàm update_time() để bắt đầu đếm ngược mới cho chế độ mới
    check_button.config(text="Check", state=tk.NORMAL)  # Thiết lập lại nút "Check"

def create_game_mode_selection():
    mode_selection_window = tk.Toplevel(root)
    mode_selection_window.title("Select Game Mode")

    def select_mode_1():
        change_game_mode(1)
        mode_selection_window.destroy()

    def select_mode_2():
        change_game_mode(2)
        mode_selection_window.destroy()

    mode1_button = tk.Button(mode_selection_window, text="Game Mode 1", command=select_mode_1, font=("Times New Roman", 20))
    mode1_button.pack(padx=20, pady=10)

    mode2_button = tk.Button(mode_selection_window, text="Game Mode 2", command=select_mode_2, font=("Times New Roman", 20))
    mode2_button.pack(padx=20, pady=10)

root = tk.Tk()
root.title("Speed Typing")
score = 0
time_left = 25  # Hoặc bất kỳ giá trị mặc định nào bạn muốn
highest_score = 0  # Tạo biến để lưu điểm cao nhất
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

# Các chức năng trong game
# Thêm một nút để mở hộp thoại chọn chế độ trò chơi
mode_button = tk.Button(root, text="Select Game Mode", command=create_game_mode_selection, font=("Times New Roman", 20))
mode_button.place(x=560, y=20)

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

# Thêm nút "Chơi lại" và gán chức năng reset_game cho nó
play_again_button = tk.Button(root, text="Reset", command=reset_game, font=("Times New Roman", 20))
play_again_button.place(x=20, y=200)

# Begin the countdown
update_time()
root.geometry("800x500")
root.mainloop()
