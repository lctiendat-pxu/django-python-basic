import random

def so_uoc_so(n):
  """Tính và trả về số các ước số thực sự của n."""
  count = 0
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      count += 2
      if i == n // i:
        count -= 1
  return count

def kiem_tra_so_nguyen_to(n):
  """Kiểm tra và trả về 1 nếu n là số nguyên tố, ngược lại trả về 0."""
  if n <= 1:
    return 0
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return 0
  return 1

def dem_so_uoc_so_le(n):
  """Đếm và trả về số các ước số lẻ của n."""
  count = 0
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      if i % 2 != 0:
        count += 1
      if i != n // i and n // i % 2 != 0:
        count += 1
  return count

def dem_so_nguyen_to(n):
  """Đếm và trả về số các số nguyên tố nhỏ hơn n."""
  count = 0
  for i in range(2, n):
    if kiem_tra_so_nguyen_to(i):
      count += 1
  return count

def tong_uoc_so(n):
  """Tính và trả về tổng tất cả các ước số thực sự của n."""
  tong = 0
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      tong += i
      if i != n // i:
        tong += n // i
  return tong

# Nhập số tự nhiên n
n = random.randint(5, 100)

# Gọi các hàm và in ra kết quả
print(f"Số ước số của {n} là: {so_uoc_so(n)}")
if kiem_tra_so_nguyen_to(n):
  print(f"{n} là số nguyên tố.")
else:
  print(f"{n} không phải là số nguyên tố.")
print(f"Số ước số lẻ của {n} là: {dem_so_uoc_so_le(n)}")
print(f"Số nguyên tố nhỏ hơn {n} là: {dem_so_nguyen_to(n)}")
print(f"Tổng các ước số của {n} là: {tong_uoc_so(n)}")
