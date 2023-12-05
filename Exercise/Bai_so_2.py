import matplotlib.pyplot as plt
import numpy as np

# Tạo một mảng các giá trị x trong khoảng từ -5 đến 5 với bước nhảy là 0.1
x = np.arange(-5, 5, 0.1)

# Tính các giá trị y tương ứng với mỗi giá trị x
y = x**2

# Vẽ đồ thị
plt.plot(x, y)

# Đặt nhãn cho trục x và trục y
plt.xlabel('x')
plt.ylabel('y')

# Đặt tiêu đề cho đồ thị
plt.title('Đồ thị hàm số y = x^2 - 2x + 1')

# Hiển thị đồ thị
plt.show()