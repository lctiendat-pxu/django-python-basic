import random

def uoc_so_chung_lon_nhat(a, b):
  """Tìm ước số chung lớn nhất của hai số a và b."""
  if b == 0:
    return a
  return uoc_so_chung_lon_nhat(b, a % b)

# Tạo danh sách A và B
A = [random.randint(30, 150) for i in range(10)]
B = [random.randint(30, 150) for i in range(10)]

# Tạo danh sách C
C = [uoc_so_chung_lon_nhat(a, b) for a, b in zip(A, B)]

# In kết quả
print(f"Danh sách A: {A}")
print(f"Danh sách B: {B}")
print(f"Danh sách C: {C}")
