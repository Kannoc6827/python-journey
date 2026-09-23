"""
Bài tập 02: Toán tử logic 🧠
==============================
Mục tiêu: Kết hợp and, or, not trong điều kiện
"""

# TODO 1: Kiểm tra đủ điều kiện lái xe
# tuoi >= 18 AND co_bang_lai == True AND khong_say == True
# kiem tra ho chieu nhap canh
ho_chieu = input("HO CHIEU (Y/N): ").lower() == "y"  
co_visa = input("VISA (Y/N): ").lower() == "y"
mien_visa = input("MIEN VISA (Y/N): ").lower() == "y"
nam_trong_danh_sach_cam = input("NAM TRONG DANH SACH CAM (Y/N): ").lower() == "y"

if nam_trong_danh_sach_cam:
    print("Khong hop le: Ban nam trong danh sach cam nhap canh!")
elif not ho_chieu:
    print("Khong hop le: Ho chieu cua ban khong hop le!")
elif not (co_visa or mien_visa):
    print("Khong hop le: Ban khong co Visa va cung khong thuoc dien mien Visa!")
else:
    print("Hop le: Ban DU dieu kien nhap canh!")

# TODO 2: Phân loại tam giác
# Nhập 3 cạnh a, b, c
# Kiểm tra: có tạo thành tam giác không? (tổng 2 cạnh > cạnh còn lại)
# Nếu có: đều, cân, hay thường?
print("Kiem tra canh tam giac")
a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Ket qua: Day la tam giac deu")
    elif a == b or b == c or a == c:
        print("Ket qua: Day la tam giac can")
    else:
        print("Ket qua: Day la tam giac thuong")
else:
    print("Ket qua: a,b,c khong phai la 3 canh cua tam giac")

# TODO 3: Kiểm tra mật khẩu mạnh
# Mật khẩu mạnh khi: >= 8 ký tự AND có chữ hoa AND có chữ thường AND có số
# Gợi ý: dùng any(c.isupper() for c in pw), any(c.islower()...), any(c.isdigit()...)
ps = input("Nhap mat khau can kiem tra: ")

length_ok = len(ps) >= 8
has_upper = any(c.isupper() for c in ps)
has_lower = any(c.islower() for c in ps)
has_digit = any(c.isdigit() for c in ps)

if length_ok and has_upper and has_lower and has_digit:
    print("Ket qua: Mat khau MANH")
else:
    print("Ket qua: Mat khau YEU (Phai co tu 8 ky tu, co chu hoa, chu thuong, ky hieu va so)")

# TODO 4 (Thử thách): FizzBuzz
# Nhập số n. In "Fizz" nếu chia hết 3, "Buzz" nếu chia hết 5,
# "FizzBuzz" nếu chia hết cả 3 và 5, ngược lại in số đó
n = int(input("Nhap so nguyen n: "))

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)


