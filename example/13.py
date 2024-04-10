import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def f(x):
  return 4*x**4 + 5*x**2 - 8

def f_prime(x):
  return 16*x**3 + 10*x

def f_second_prime(x):
  return 48*x**2 + 10

def f_third_prime(x):
  return 96*x

# Tạo mảng giá trị x
x = np.linspace(-15, 15, 1000)

# Tính giá trị y, y', y'', y'''
y = f(x)
y_prime = f_prime(x)
y_second_prime = f_second_prime(x)
y_third_prime = f_third_prime(x)

# Vẽ đồ thị
plt.plot(x, y, label='y')
plt.plot(x, y_prime, label="y'")
plt.plot(x, y_second_prime, label="y''")
plt.plot(x, y_third_prime, label="y'''")

# Thiết lập nhãn trục
plt.xlabel('x')
plt.ylabel('y')

# Hiển thị chú thích
plt.legend()

# Hiển thị hình
plt.show()
