import othermodule
import random
import math
# Sinh số ngẫu nhiên
a = random.randint(1, 70)
b = random.randint(1, 5)
c = random.randint(1, 150)

# Gọi các hàm trong module sinhvien
tong = othermodule.cong(a, b)
tich = othermodule.nhan(a, b)
mu = othermodule.mu(a, b)
can_bac_2 = othermodule.can_bac_2(a)
acos = othermodule.acos(a)
ptb2 = othermodule.giai_ptb2(a, b, c)

# In kết quả
print(f"Tổng: {a} + {b} = {tong}")
print(f"Tích: {a} * {b} = {tich}")
print(f"Mũ: {a} ** {b} = {mu}")
print(f"Căn bậc 2 của {a}: √{a} = {can_bac_2}")
print(f"acos({a}) = {acos}")
print(f"Phương trình bậc 2 {a}x^2 + {b}x + {c} = 0: {ptb2}")
