import random

def kiem_tra_so_nguyen_to(n):
  """Kiểm tra và trả về 1 nếu n là số nguyên tố, ngược lại trả về 0."""
  if n <= 1:
    return 0
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      return 0
  return 1

def tong_so_nguyen_to(n):
  """Tính và trả về tổng các số nguyên tố nhỏ hơn n."""
  tong = 0
  for i in range(2, n):
    if kiem_tra_so_nguyen_to(i):
      tong += i
  return tong

def tong_uoc_so(n):
  """Tính và trả về tổng tất cả các ước số thực sự của n."""
  tong = 0
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      tong += i
      if i != n // i:
        tong += n // i
  return tong

def tong_so_le_for(n):
  """Tính và trả về tổng các số lẻ từ 1 đến n bằng vòng lặp for."""
  tong = 0
  for i in range(1, n + 1, 2):
    tong += i
  return tong

def tong_so_le_while(n):
  """Tính và trả về tổng các số lẻ từ 1 đến n bằng vòng lặp while."""
  tong = 0
  i = 1
  while i <= n:
    tong += i
    i += 2
  return tong

# Nhập số tự nhiên n
n = random.randint(10, 100)

# Tính tổng các số nguyên tố nhỏ hơn n
tong_so_nguyen_to = tong_so_nguyen_to(n)

# Tính tổng các ước số của n
tong_uoc_so = tong_uoc_so(n)

# Tính tổng các số lẻ từ 1 đến n bằng vòng lặp for
tong_so_le_for = tong_so_le_for(n)

# Tính tổng các số lẻ từ 1 đến n bằng vòng lặp while
tong_so_le_while = tong_so_le_while(n)

# In ra kết quả
print(f"Tổng các số nguyên tố nhỏ hơn {n} là: {tong_so_nguyen_to}")
print(f"Tổng các ước số của {n} là: {tong_uoc_so}")
print(f"Tổng các số lẻ từ 1 đến {n} bằng vòng lặp for: {tong_so_le_for}")
print(f"Tổng các số lẻ từ 1 đến {n} bằng vòng lặp while: {tong_so_le_while}")
