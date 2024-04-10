import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



A = np.linspace(0, 2*np.pi, 100)
B = np.linspace(0, np.pi, 100)

# Tạo tọa độ x, y, z của mặt cầu
X = np.outer(np.sin(B), np.cos(A))
Y = np.outer(np.sin(B), np.sin(A))
Z = np.outer(np.cos(B), np.ones_like(A))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Vẽ mặt cầu
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Thiết lập nhãn trục
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Thêm thanh màu
plt.colorbar(ax.get_children()[0])

# Hiển thị hình
plt.show()

