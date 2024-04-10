import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)

# Tạo hàm mặt yên ngựa
Z = 0.5 * (X**2 - Y**2)

fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection='3d')

# Vẽ mặt yên ngựa
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Thiết lập nhãn trục
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Thêm thanh màu
plt.colorbar(ax.get_children()[0])

# Hiển thị hình
plt.show()