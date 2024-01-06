import requests
from PIL import ImageTk, Image
from tkinter import Tk, Entry, Button, Label, messagebox  # Thêm các thư viện cần thiết từ Tkinter

# Lấy dữ liệu thời tiết
def get_weather(city):
    API_key = "6b269ca87de134acdbfbdb5da3c24be7"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    # kiểm tra nếu input nhập vào không hợp lệ trả về hộp thư 404
    if res.status_code == 404:
        messagebox.showerror("LỖI", "KHÔNG TÌM THẤY THÀNH PHỐ !!!")
        return None

    # URL ảnh biểu tượng, nhiệt độ, trạng thái thời tiết, tên thành phố, tên quốc gia.
    Weather = res.json()
    icon_id = Weather['weather'][0]['icon']
    temperature = Weather['main']['temp'] - 273.15
    description = Weather['weather'][0]['description']
    city = Weather['name']
    country = Weather['sys']['country']

    icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return (icon_url, temperature, description, city, country)

# gọi hàm tìm kiếm khi nhấn nút "Search".
def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return

    # Gán các giá trị trả về từ hàm get_weather.
    icon_url, temperature, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temperature_label.configure(text=f"NHIỆT ĐỘ: {temperature:.2f}ºC")
    description_label.configure(text=f"TÌNH TRẠNG THỜI TIẾT: {description}")

# Tạo cửa sổ chính của ứng dụng.
root = Tk()
root.title("DỰ BÁO THỜI TIẾT")
root.geometry("600x400")

# Tạo input field để nhập tên thành phố.
city_entry = Entry(root, font="Helvetica, 25")
city_entry.pack(pady=15)

search_button = Button(root, text="Search", command=search)
search_button.pack(pady=15)

# Tạo nhãn để hiển thị tên thành phố và quốc gia.
location_label = Label(root, font="Helvetica, 25")
location_label.pack(pady=15)

# Tạo nhãn để hiển thị ảnh biểu tượng thời tiết.
icon_label = Label(root)
icon_label.pack()

# Tạo nhãn để hiển thị giá trị nhiệt độ.
temperature_label = Label(root, font="Helvetica, 25")
temperature_label.pack()

# Tạo nhãn để hiển thị mô tả thời tiết.
description_label = Label(root)
description_label.pack()

# Khởi động ứng dụng và chờ đợi sự kiện.
root.mainloop()
