try:
  a = float(input("Nhập độ dài cạnh a: "))
  b = float(input("Nhập độ dài cạnh b: "))
  c = float(input("Nhập độ dài cạnh c: "))
except ValueError:
  print("Lỗi: Vui lòng nhập số cho độ dài cạnh.")
  exit()

if a <= 0 or b <= 0 or c <= 0:
  print("Lỗi: Độ dài cạnh phải là số dương.")
  exit()

if a + b <= c or a + c <= b or b + c <= a:
  print("Lỗi: Ba cạnh không thể tạo thành tam giác.")
  exit()

print("Ba cạnh a, b, c hợp lệ để tạo thành tam giác.")
