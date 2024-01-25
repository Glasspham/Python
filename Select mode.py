import tkinter as tk

def thay_doi_label():
    selected_option = v.get()  # Lấy giá trị của Radiobutton đã chọn
    label.config(text=f"Tùy chọn {selected_option}")  # Thay đổi label theo giá trị đã chọn

root = tk.Tk()
root.title("Thay đổi Label")

v = tk.IntVar()

# Tạo Radiobuttons
for i in range(1, 4):
    tk.Radiobutton(root, text=f"Chọn {i}", variable=v, value=i, command=thay_doi_label).pack()

# Label ban đầu
label = tk.Label(root, text="Tùy chọn")
label.pack()

root.mainloop()
