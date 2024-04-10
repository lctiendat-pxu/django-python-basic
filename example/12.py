import numpy as np

# Sinh ngẫu nhiên số hàng và cột
m, n = np.random.randint(3, 9, size=2)

# Tạo ma trận A và B với các phần tử ngẫu nhiên
A = np.random.rand(m, n)
B = np.random.rand(m, n)

# a) Tích vô hướng hai ma trận
def dot_product(A, B):
    return np.dot(A, B.T)  # B.T là ma trận chuyển vị của B

# b) Tích có hướng hai ma trận
def cross_product(A, B):
    return np.cross(A, B)  # Bt không cần thiết vì np.cross đã tính tích có hướng

# c) Chương trình chính
D = dot_product(A, B)
# E = cross_product(A, B)  # Chỉ thực hiện được khi m = n = 3

print(D)
