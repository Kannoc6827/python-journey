"""
Bài tập 03: f-string formatting 💅
====================================
Mục tiêu: Định dạng output đẹp với f-string
"""

# TODO 1: Cho ten = "An", tuoi = 20, diem = 8.567
# In ra: "Học sinh An, 20 tuổi, điểm TB: 8.57"
# Gợi ý: dùng :.2f để làm tròn 2 chữ số thập phân
ten = "An"
tuoi = 20
diem = 8.567
print(f"Hoc sinh {ten}, {tuoi} tuoi, diem TB: {diem:.2f}")
# TODO 2: In bảng cửu chương 5 với cột thẳng hàng
# Dùng f-string width: f"{value:>4}"
# 5 x  1 =   5
# 5 x  2 =  10
# ...
# 5 x 10 =  50

for i in range(1, 11):
    print(f"5 x {i:>2} = {5 * i:>4}")

# TODO 3: In hóa đơn mua hàng đẹp
# Dùng f-string để căn lề trái/phải
# ===========================
# SẢN PHẨM          GIÁ (VNĐ)
# ---------------------------
# Cà phê              35,000
# Bánh mì             25,000
# Nước suối            10,000
# ---------------------------
# TỔNG CỘNG           70,000
# ===========================
# Gợi ý: dùng f"{name:<20}{price:>10,}"

sp1_ten, sp1_gia = "Ca phe", 35000
sp2_ten, sp2_gia = "Banh mi", 25000
sp3_ten, sp3_gia = "Nuoc suoi", 10000

tong_cong = sp1_gia + sp2_gia + sp3_gia

print("=" * 35)
print(f"{'SAN PHAM':<22}{'GIA (VND)':>13}")
print("-" * 35)
print(f"{sp1_ten:<22}{sp1_gia:>13,}")
print(f"{sp2_ten:<22}{sp2_gia:>13,}")
print(f"{sp3_ten:<22}{sp3_gia:>13,}")
print("-" * 35)
print(f"{'TONG CONG':<22}{tong_cong:>13,}")
print("=" * 35)

# TODO 4 (Thử thách): Tạo progress bar bằng f-string
# Nhập phần trăm (0-100)
# In ra: [████████░░░░░░░░░░░░] 40%
percent = int(input("Nhap phan tram (0-100): "))

# Dam bao gia tri trong khoang 0-100
percent = max(0, min(100, percent))

# Quy doi 100% thanh thanh dai 20 ky tu (moi 5% = 1 ky tu)
total_blocks = 20
filled_length = int(total_blocks * percent // 100)
empty_length = total_blocks - filled_length

# Tao chuoi block va empty
bar = "|||" * filled_length + "___" * empty_length

print(f"[{bar}] {percent}%")