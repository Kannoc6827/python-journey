"""
Bài tập 01: if/elif/else cơ bản 🔀
====================================
Mục tiêu: Viết câu lệnh điều kiện đúng cú pháp
"""

# TODO 1: Nhập tuổi, in ra nhóm tuổi
# < 13: "Thiếu nhi"
# 13-17: "Thiếu niên"
# 18-64: "Người lớn"
# >= 65: "Người cao tuổi"

tuoi = int(input("Nhap tuoi cua ban: "))
if tuoi < 13:
    print("Ban la thieu Nhi")
elif 13 < tuoi <= 17:
    print("Ban la thieu nien")
elif 18 < tuoi <= 64:
    print("Ban la nguoi lon")
else:
    print("Ban la nguoi cao tuoi")

# TODO 2: Nhập điểm (0-10), xếp loại:
# >= 9: Xuất sắc, >= 8: Giỏi, >= 6.5: Khá, >= 5: TB, < 5: Yếu

diem = float(input("Nhap diem cua ban (0-10): "))
if diem >= 9:
    print("Ban la hoc sinh Xuat sac")
elif diem >= 8:
    print("Ban la hoc sinh Gioi")
elif diem >= 6.5:
    print("Ban la hoc sinh Kha")
elif diem >= 5:
    print("Ban la hoc sinh Trung binh")
else:
    print("Ban la hoc sinh Yeu")

# TODO 3: Nhập năm, kiểm tra năm nhuận
# Năm nhuận: chia hết cho 4, NHƯNG không chia hết cho 100,
# TRỪ KHI chia hết cho 400
# 2000 → nhuận, 1900 → không, 2024 → nhuận

nam = int(input("Hay nhap nam ban muon kiem tra nam nhuan: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    print(f"{nam} la nam nhuan")
else:
    print(f"{nam} la nam khong nhuan")

# TODO 4 (Thử thách): Nhập 3 số, in ra số lớn nhất
# KHÔNG dùng hàm max() — chỉ dùng if/elif/else
print("Kiem tra so lon nhat trong cac so")
a = float(input("So thu nhat: "))
b = float(input("So thu hai: "))
c = float(input("So thu ba: "))
if a >= b and a >= c:
    print(f"So lon nhat: {a}")
elif b >= a and b >= c:
    print(f"So lon nhat: {b}")
else:
    print(f"So lon nhat: {c}")