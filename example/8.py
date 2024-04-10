import random

def doc_du_lieu(fin):
  """Đọc dữ liệu từ tệp fin.txt."""
  with open(fin, "r") as f:
    n = int(f.readline())
    mang_tong = []
    for i in range(n):
      mang_so = list(map(float, f.readline().split()))
      tong = sum(mang_so)
      mang_tong.append(tong)
    return n, mang_tong


def ghi_du_lieu(fout, n, S, mang_tong):
  """Ghi dữ liệu vào tệp fout.txt."""
  with open(fout, "w") as f:
    f.write(f"{S}\n")
    for i in range(n):
      f.write(f"{mang_tong[i]}\n")


fin = "fin.txt"
fout = "fout.txt"

# Đọc dữ liệu từ tệp fin.txt
n, mang_tong = doc_du_lieu(fin)

# Tính tổng S
S = sum(mang_tong)

# Ghi dữ liệu vào tệp fout.txt
ghi_du_lieu(fout, n, S, mang_tong)
