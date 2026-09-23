"""
Bài tập 03: Điều kiện lồng nhau 🪆
====================================
Mục tiêu: Xử lý logic phức tạp với if lồng nhau
"""

# TODO 1: ATM rút tiền
# Nhập số dư hiện tại và số tiền muốn rút
# Kiểm tra: số tiền rút > 0? Đủ số dư không? Bội số 50,000?
# In thông báo phù hợp
so_du = float(input("Nhap so du hien tai: "))
so_tien_rut = float(input("Nhap so tien muon rut: "))

if so_tien_rut <= 0:
    print("Loi: So tien rut phai lon hon 0!")
elif so_tien_rut > so_du:
    print("Loi: So du khong du de thuc hien giao dich!")
elif so_tien_rut % 50000 != 0:
    print("Loi: So tien rut phai la boi so cua 50,000 VND!")
else:
    so_du_con_lai = so_du - so_tien_rut
    print(f"Rut tien thanh cong: {so_tien_rut:,.0f} VND")
    print(f"So du con lai: {so_du_con_lai:,.0f} VND")

# TODO 2: Xếp loại BMI
# Nhập chiều cao (m) và cân nặng (kg)
# BMI = weight / height^2
# < 18.5: Thiếu cân → gợi ý tăng cân
# 18.5-24.9: Bình thường → khen
# 25-29.9: Thừa cân → cảnh báo nhẹ
# >= 30: Béo phì → khuyến nghị gặp bác sĩ
height = float(input("Nhap chieu cao (m): "))
weight = float(input("Nhap can nang (kg): "))

bmi = weight / (height ** 2)
print(f"Chi so BMI cua ban: {bmi:.2f}")

if bmi < 18.5:
    print("Xep loai: Thieu can")
    print("Goi y: Ban nen tang cuong dinh duong va tap luyen de tang can")
elif 18.5 <= bmi <= 24.9:
    print("Xep loai: Binh thuong")
    print("Loi khuyen: Tuyet voi! Hay tiep tuc duy tri che do sinh hoat nay")
elif 25 <= bmi <= 29.9:
    print("Xep loai: Thua can")
    print("Canh bao: Nen giam an do ngot, chat bao va tang cuong van dong")
else:
    print("Xep loai: Beo phi")
    print("Khuyen nghi: Ban nen gap bac si/chuyen gia dinh duong de duoc tu van")

# TODO 3: Máy bán vé xem phim
# Nhập: loại vé (thuong/vip), ngày (thuong/cuoi_tuan), tuổi
# Giá cơ bản: thường 80k, VIP 120k
# Cuối tuần: +30%
# Trẻ em (<12) và người cao tuổi (>=65): giảm 50%
# Sinh viên (18-25): giảm 20%
# In giá vé cuối cùng
loai_ve = input("Nhap loai ve (thuong/vip): ").lower()
ngay = input("Nhap ngay xem (thuong/cuoi_tuan): ").lower()
tuoi = int(input("Nhap tuoi cua ban: "))

if loai_ve == "vip":
    gia_ve = 120000
else:
    gia_ve = 80000

if ngay == "cuoi_tuan":
    gia_ve *= 1.3

if tuoi < 12 or tuoi >= 65:
    gia_ve *= 0.5  # Giam 50%
elif 18 <= tuoi <= 25:
    is_sv = input("Ban co phai sinh vien khong? (Y/N): ").lower() == "y"
    if is_sv:
        gia_ve *= 0.8  # Giam 20%

print(f"Gia ve cuoi cung cua ban la: {gia_ve:,.0f} VND")