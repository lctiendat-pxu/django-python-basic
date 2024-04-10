import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_saddle(x_range, y_range):
  """Vẽ đồ thị mặt yên ngựa z = (x/4)^2 - (y/5)^2."""
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111, projection='3d')

  # Tạo dữ liệu
  x, y = np.meshgrid(x_range, y_range)
  z = (x/4)**2 - (y/5)**2

  # Vẽ mặt
  ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

  # Thiết lập nhãn trục
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')

  # Hiển thị hình
  plt.show()


def plot_hyperboloid(x_range, y_range):
  """Vẽ đồ thị mặt hyperbolic 1 tầng (x/5)^2 + (y/3)^2 - (z/4)^2 = 1."""
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111, projection='3d')

  # Tạo dữ liệu
  x, y = np.meshgrid(x_range, y_range)
  z = np.sqrt((x/5)**2 + (y/3)**2 + 1)

  # Vẽ mặt
  ax.plot_surface(x, y, z, cmap='hot', alpha=0.8)

  # Thiết lập nhãn trục
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')

  # Hiển thị hình
  plt.show()


def plot_sphere(x_range, y_range, z_range):
  """Vẽ đồ thị mặt cầu (x + 6)^2 + (y - 3)^2 + (z - 8)^2 = 6."""
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111, projection='3d')

  # Tạo lưới điểm
  x = np.linspace(*x_lim, 200)
  y = np.linspace(*y_lim, 200)
  z = np.linspace(*z_lim, 200)
  X, Y, Z = np.meshgrid(x, y, z)

  # Tính f(x, y, z)
  F = (X + 6)**2 + (Y - 3)**2 + (Z - 8)**2 - 6

  # Vẽ mặt
  ax.plot_surface(X[F == 0], Y[F == 0], Z[F == 0], cmap='viridis', alpha=0.8)

  # Thiết lập nhãn trục
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')

  # Thêm thanh màu
  plt.colorbar(ax.get_children()[0])

  plt.show()


# Vẽ mặt yên ngựa
plot_saddle(np.linspace(-10, 10, 200), np.linspace(-10, 10, 200))

# Vẽ mặt hyperbolic 1 tầng
plot_hyperboloid(np.linspace(-10, 10, 200), np.linspace(-10, 10, 200))

# Vẽ mặt cầu
plot_sphere(np.linspace(-15, 3, 200), np.linspace(-2, 8, 200), np.linspace(2, 14, 200))
