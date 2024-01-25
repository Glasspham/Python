import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Tạo một đối tượng figure
fig = plt.figure()

# Tạo một đối tượng axes với chiếu 3D
ax = fig.add_subplot(111, projection='3d')

# Định nghĩa các đỉnh của hình lập phương
vertices = np.array([[0, 0, 0], [255, 0, 0], [255, 255, 0], [0, 255, 0], [0, 0, 255], [255, 0, 255], [255, 255, 255], [0, 255, 255]])

# Định nghĩa các cạnh của hình lập phương
edges = [(0, 1), (0, 3), (0, 4), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (4, 5), (4, 7), (5, 6), (6, 7)]

# Định nghĩa các màu của các đỉnh
colors = ['Black', 'Red', 'Yellow', 'Green', 'Blue', 'Magenta', 'White', 'Cyan']

# Vẽ các đỉnh, các cạnh và các chú thích
for i in range(len(vertices)):
    # Vẽ một điểm màu với màu tương ứng
    ax.scatter(vertices[i, 0], vertices[i, 1], vertices[i, 2], color=colors[i])
    # Thêm một chú thích cho điểm màu với tên màu và tọa độ
    ax.text(vertices[i, 0], vertices[i, 1], vertices[i, 2], f'{colors[i]}={tuple(vertices[i])}')
for edge in edges:
    # Kiểm tra xem cạnh có phải là một trong ba cạnh mong muốn hay không
    if edge in [(0, 3), (0, 4), (0, 1)]:
        # Vẽ một đường nối hai điểm màu với màu đen và kiểu nét đứt
        ax.plot([vertices[edge[0], 0], vertices[edge[1], 0]], [vertices[edge[0], 1], vertices[edge[1], 1]], [vertices[edge[0], 2], vertices[edge[1], 2]], color='black', linestyle='--', label=f'{colors[edge[0]]}-{colors[edge[1]]}')
    else:
        # Vẽ một đường nối hai điểm màu với màu đen và kiểu nét liền
        ax.plot([vertices[edge[0], 0], vertices[edge[1], 0]], [vertices[edge[0], 1], vertices[edge[1], 1]], [vertices[edge[0], 2], vertices[edge[1], 2]], color='black', linestyle='-')

# Vẽ mũi tên
ax.quiver(0, 0, 255, 0, 0, 100, color='black')  # Mũi tên từ điểm Blue
ax.quiver(0, 255, 0, 0, 100, 0, color='black')  # Mũi tên từ điểm Green
ax.quiver(255, 0, 0, 100, 0, 0, color='black')  # Mũi tên từ điểm Red

# Thêm các nhãn cho các trục
ax.set_xlabel('B')
ax.set_ylabel('R')
ax.set_zlabel('G')

# Ẩn các trục và đường lưới
ax.set_axis_off()
ax.grid(False)

# Đặt màu nền là trắng
ax.set_facecolor('white')

# Hiển thị đồ thị
plt.show()
