import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import re
from PIL import Image, ImageTk

# Fix khi user nhập vào
def parse_function(function):
    # Thay thế các ký tự '^' bằng '**' cho phép toán mũ
    function = function.replace('^', '**')
    
    # Thay thế các ký hiệu tuyệt đối
    function = re.sub(r'\|([^|]+)\|', r'np.abs(\1)', function)
    
    # Thay thế 'ln' thành 'np.log'
    function = function.replace('ln', 'np.log')
    
    # Thay thế 'log_b(x)' thành 'np.log(x)/np.log(b)'
    function = re.sub(r'log(\d+)\((.*?)\)', r'np.log(\2)/np.log(\1)', function)
    
    # Thay thế các hàm toán học phổ biến
    functions_list = ['sin', 'cos', 'tan', 'sqrt', 'exp']
    for func in functions_list:
        function = re.sub(rf'\b{func}\b', f'np.{func}', function)
    
    # Xử lý e^x và thêm dấu ngoặc đóng sau np.exp
    function = re.sub(r'\be\^(\w+)', r'np.exp(\1)', function)
    
    # Thay thế các ký tự nối nhau không hợp lệ
    function = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', function)
    function = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', function)
    function = re.sub(r'(\))(\()', r'\1*\2', function)
    function = re.sub(r'(\d)(\()', r'\1*\2', function)
    function = re.sub(r'(\))(\d)', r'\1*\2', function)
    
    return function

# Fix hiển hàm trên đồ thị
def display_function(function):
    function = function.replace('**', '^')
    function = function.replace('np.abs', '|')
    function = function.replace('np.log', 'ln')
    function = re.sub(r'np.log\((.*?)\)/np.log\((\d+)\)', r'log\2(\1)', function)
    function = function.replace('np.exp', 'e^')
    function = re.sub(r'\*', '', function)
    return function

# Xử lý vẽ đồ thị
def plot_function():
    if function_entries:
        try:
            x = np.linspace(-10, 10, 400) # (start,end,step)
            fig, ax = plt.subplots()

            for entry in function_entries:
                function = entry.get()
                if function:
                    parsed_function = parse_function(function)
                    y = eval(parsed_function)
                    ax.plot(x, y, label=f"y = {display_function(function)}")

            ax.set_xlabel("x")
            ax.set_ylabel("y")
            ax.set_title("Đồ thị hàm số")
            ax.legend()
            ax.grid(True)
            ax.axhline(0, color='black', linewidth=0.5)
            ax.axvline(0, color='black', linewidth=0.5)

            # Mở cửa sổ mới và hiển thị đồ thị trong đó
            new_window = tk.Toplevel(root)
            new_window.title(f"Đồ thị {len(root.children) - 2}")

            # Hiển thị đồ thị trong cửa sổ mới
            canvas = FigureCanvasTkAgg(fig, master=new_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        except Exception as e:
            messagebox.showerror("Error", f"Có lỗi xảy ra: {e}")

# Reset lại cửa sổ
def reset_plot():
    for widget in root.winfo_children():
        widget.destroy()
    
    # Hiển thị lại hình nền
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Tạo lại các khung nhập liệu và nút bấm
    create_widgets()

# Giúp chương trình dừng lại sau khi người dùng nhấn vào x
def on_closing():
    root.quit()
    root.destroy()

# Thanh cho user nhập hàm
def add_function_entry():
    entry = tk.Entry(root, width=100)
    entry.pack(pady=10)
    function_entries.append(entry)

# Design display
def create_widgets():
    global function_entries
    function_entries = []

    # Tạo một khung để chứa các nút
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Nút thêm hàm số
    add_button = tk.Button(button_frame, text="Thêm hàm số", command=add_function_entry, font=("Arial", 14), padx=10, pady=5)
    add_button.pack(side=tk.LEFT, padx=5)

    # Tạo nút bấm để vẽ đồ thị
    plot_button = tk.Button(button_frame, text="Vẽ đồ thị", command=plot_function, font=("Arial", 14), padx=10, pady=5)
    plot_button.pack(side=tk.LEFT, padx=5)

    # Tạo nút reset để xóa đồ thị và nhập hàm số mới
    reset_button = tk.Button(button_frame, text="Reset", command=reset_plot, font=("Arial", 14), padx=10, pady=5)
    reset_button.pack(side=tk.LEFT, padx=5)

    # Khung nhập liệu đầu tiên
    tk.Label(root, text="Nhập hàm số f(x):", font=("Arial", 16)).pack(pady=10)
    add_function_entry()

# Hàm chính để gọi tất cả
if __name__ == "__main__":
    # Tạo cửa sổ tkinter
    root = tk.Tk()
    root.title("Vẽ đồ thị hàm số")

    # Đảm bảo rằng chương trình sẽ dừng hoàn toàn khi cửa sổ chính bị đóng
    root.protocol("WM_DELETE_WINDOW", on_closing)

    # Chỉnh kích thước cửa sổ
    root.geometry("900x700")

    # Đặt hình nền cho cửa sổ chính
    image = Image.open("background.jpg")
    image = image.resize((900, 700))
    background_image = ImageTk.PhotoImage(image)
    background_label = tk.Label(root, image=background_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Tạo các khung nhập liệu và nút bấm
    create_widgets()

    # Chạy vòng lặp chính của tkinter
    root.mainloop()
