class NhanVien:
  def __init__(self, hoten, tuoi, luong):
    self.hoten = hoten
    self.tuoi = tuoi
    self.luong = luong

  def __str__(self):
    return f"Họ tên: {self.hoten}\nTuổi: {self.tuoi}\nLương: {self.luong}"


def nhap_danh_sach_nhan_vien():
  """Nhập dữ liệu cho danh sách nhân viên."""
  ds_nhan_vien = []
  n = int(input("Nhập số lượng nhân viên: "))
  for i in range(n):
    hoten = input("Nhập họ tên nhân viên: ")
    tuoi = int(input("Nhập tuổi nhân viên: "))
    luong = float(input("Nhập lương nhân viên: "))
    nhan_vien = NhanVien(hoten, tuoi, luong)
    ds_nhan_vien.append(nhan_vien)
  return ds_nhan_vien


def sap_xep_theo_tuoi(ds_nhan_vien):
  """Sắp xếp danh sách nhân viên theo tuổi giảm dần."""
  ds_nhan_vien.sort(key=lambda nv: nv.tuoi, reverse=True)

def in_danh_sach_nhan_vien(ds_nhan_vien):
  """In danh sách nhân viên."""
  for nhan_vien in ds_nhan_vien:
    print(nhan_vien)
    print()


def ghi_file_nhan_vien(ds_nhan_vien):
  """Ghi danh sách nhân viên vào tập tin."""
  with open("NhanVien.txt", "w") as f:
    for nhan_vien in ds_nhan_vien:
      f.write(f"{nhan_vien.hoten},{nhan_vien.tuoi},{nhan_vien.luong}\n")


def doc_file_nhan_vien():
  """Đọc file nhân viên và in ra màn hình."""
  with open("NhanVien.txt", "r") as f:
    for line in f:
      hoten, tuoi, luong = line.split(",")
      nhan_vien = NhanVien(hoten, int(tuoi), float(luong))
      print(nhan_vien)
      print()

# Nhập danh sách nhân viên
ds_nhan_vien = nhap_danh_sach_nhan_vien()

# Sắp xếp danh sách nhân viên theo tuổi giảm dần
sap_xep_theo_tuoi(ds_nhan_vien)

# In danh sách nhân viên
print("Danh sách nhân viên:")
in_danh_sach_nhan_vien(ds_nhan_vien)

# Ghi danh sách nhân viên vào tập tin
ghi_file_nhan_vien(ds_nhan_vien)

# Đọc file nhân viên và in ra màn hình
print("Danh sách nhân viên từ file:")
doc_file_nhan_vien()
