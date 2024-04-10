def diem_lon_nhat(diem):
  """Tìm và in ra điểm lớn nhất trong từ điển."""
  diem_max = max(diem.values())
  print(f"Điểm lớn nhất là: {diem_max}")

def mon_diem_cao_nhat(diem):
  """Tìm và in ra môn và điểm có điểm lớn nhất trong từ điển."""
  diem_max = max(diem.values())
  mon_diem_cao_nhat = [mon for mon, diem in diem.items() if diem == diem_max][0]
  print(f"Môn và điểm cao nhất là: {mon_diem_cao_nhat}, {diem_max}")

def diem_so_le(diem):
  """In ra các môn và điểm số lẻ trong từ điển."""
  print("Môn và điểm số lẻ:")
  for mon, diem in diem.items():
    if diem % 2 != 0:
      print(f"{mon}: {diem}")

def trung_binh_diem(diem):
  """Tính và in ra trung bình tất cả các điểm trong từ điển."""
  tong_diem = sum(diem.values())
  so_mon = len(diem)
  diem_trung_binh = tong_diem / so_mon
  print(f"Điểm trung bình là: {diem_trung_binh}")

def diem_tren_6(diem):
  """Tạo và trả về từ điển mới với các môn có điểm lớn hơn 6."""
  diem_moi = {}
  for mon, diem in diem.items():
    if diem > 6:
      diem_moi[mon] = diem
  return diem_moi

def dao_nguoc_tu_dien(diem):
  """Đảo ngược từ điển, key thành value và ngược lại."""
  diem_dao_nguoc = {diem: mon for mon, diem in diem.items()}
  return diem_dao_nguoc

diem = {"Toan": 10, "Van": 5, "Su": 8, "Dia": 7, "Hoa": 6, "Sinh": 9}

# Gọi các hàm
diem_lon_nhat(diem)
mon_diem_cao_nhat(diem)
diem_so_le(diem)
trung_binh_diem(diem)
diem_moi = diem_tren_6(diem)
print(f"Từ điển mới với các môn có điểm lớn hơn 6: {diem_moi}")
diem_dao_nguoc = dao_nguoc_tu_dien(diem)
print(f"Từ điển đảo ngược: {diem_dao_nguoc}")
