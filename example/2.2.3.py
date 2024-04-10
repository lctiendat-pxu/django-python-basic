import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from math import *

x = np.linspace(-2, 2, 200)
y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)

# z = sqrt(x^2 + y^2)

# Tạo hàm Hyperbolic một tầng
Z = np.sqrt(X**2 + Y**2)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Vẽ mặt Hyperbolic một tầng
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Thiết lập nhãn trục
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Thêm thanh màu
plt.colorbar(ax.get_children()[0])

# Hiển thị hình
plt.show()
