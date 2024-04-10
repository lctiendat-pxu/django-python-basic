import random
import string

def sinh_xau_ky_tu(n):
  """Sinh xâu ký tự ngẫu nhiên gồm n ký tự."""
  alphabet = string.ascii_lowercase
  return "".join(random.choice(alphabet) for i in range(n))

def kiem_tra_xau(Str1, Str2):
  """Kiểm tra xem xâu Str2 có nằm trong Str1 hay không."""
  return Str2 in Str1

def dem_so_lan_xuat_hien(Str1, Str2):
  """Đếm số lần xuất hiện của Str2 trong Str1."""
  count = 0
  pos = Str1.find(Str2)
  while pos != -1:
    count += 1
    pos = Str1.find(Str2, pos + len(Str2))
  return count

def chen_xau(Str1, Str2, k):
  """Chèn xâu Str2 vào Str1 tại vị trí k."""
  return Str1[:k] + Str2 + Str1[k:]

Str1 = sinh_xau_ky_tu(2)
Str2 = sinh_xau_ky_tu(30)

# Kiểm tra Str2 có nằm trong Str1 hay không
if kiem_tra_xau(Str1, Str2):
  print(f"Xâu Str2 nằm trong Str1.")
else:
  print(f"Xâu Str2 không nằm trong Str1.")

# Đếm số lần xuất hiện của Str2 trong Str1
so_lan_xuat_hien = dem_so_lan_xuat_hien(Str1, Str2)
print(f"Xâu Str2 xuất hiện {so_lan_xuat_hien} lần trong Str1.")

# Sinh số k ngẫu nhiên
k = random.randint(1, len(Str1))

# Chèn xâu Str2 vào Str1 tại vị trí k
Str1_moi = chen_xau(Str1, Str2, k)

print(f"Xâu sau khi chèn: {Str1_moi}")
