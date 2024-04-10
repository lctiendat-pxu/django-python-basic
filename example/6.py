import random

def sinh_tap_hop_A():
  """Tạo và trả về tập hợp A gồm 100 số tự nhiên ngẫu nhiên trong khoảng [1, 1000]."""
  A = set()
  while len(A) < 100:
    A.add(random.randint(1, 1000))
  return A

def sinh_tap_hop_B(A):
  """Sinh tập hợp B gồm 20 số tự nhiên ngẫu nhiên lấy từ tập hợp A."""
  B = set()
  while len(B) < 20:
    B.add(random.choice(list(A)))
  return B


def sinh_tap_hop_C(B):
  """Sinh tập hợp C gồm 10 số tự nhiên ngẫu nhiên lấy từ tập hợp B."""
  C = set()
  while len(C) < 10:
    C.add(random.choice(list(B)))
  return C


# Sinh tập hợp A
A = sinh_tap_hop_A()

# Sinh tập hợp B
B = sinh_tap_hop_B(A)

# Sinh tập hợp C
C = sinh_tap_hop_C(B)

# In kết quả
print(f"Tập hợp A: {A}")
print(f"Tập hợp B: {B}")
print(f"Tập hợp C: {C}")
