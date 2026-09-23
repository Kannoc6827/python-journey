"""
Bài tập 01: Indexing & Slicing chuỗi 🔤
=========================================
Mục tiêu: Thành thạo truy cập và cắt chuỗi
"""

# TODO 1: Cho s = "Python Journey"
# In ra: ký tự đầu, ký tự cuối (dùng index âm), 5 ký tự đầu
s = "Python Journey"
ky_tu_dau = s[0]
ky_tu_cuoi = s[-1]
nam_ky_tu_dau = s[:5]

print(f"Ky tu dau: {ky_tu_dau}")
print(f"Ky tu cuoi: {ky_tu_cuoi}")
print(f"5 ky tu dau: {nam_ky_tu_dau}")

# TODO 2: Dùng slicing để:
# a) Lấy "Journey" từ s
# b) Đảo ngược chuỗi s
# c) Lấy mỗi ký tự thứ 2 từ s

journey = s[7:]
print(f"a) Lay 'Journey': {journey}")
s_dao_nguoc = s[::-1]
print(f"b) Dao nguoc chuoi: {s_dao_nguoc}")
moi_ky_tu_thu_2 = s[::2]
print(f"c) Lay moi ky tu thu 2: {moi_ky_tu_thu_2}")

# TODO 3: Nhập CCCD (12 chữ số)
# In ra: mã tỉnh (2 số đầu), giới tính (số thứ 3), năm sinh (2 số tiếp)
# Ví dụ: "001099012345" → Tỉnh: 00, Giới tính: 1, Năm sinh: 099
cccd = input("Nhap so CCCD (12 chu so): ")

# Kiem tra do dai hop le
if len(cccd) == 12 and cccd.isdigit():
    ma_tinh = cccd[:2]       
    gioi_tinh = cccd[2]        
    nam_sinh = cccd[3:6]       
    print(f"Ma tinh: {ma_tinh}")
    print(f"Gioi tinh: {gioi_tinh}")
    print(f"Nam sinh: {nam_sinh}")
else:
    print("Loi: So CCCD phai bao gom dung 12 chu so!")

# TODO 4 (Thử thách): Kiểm tra chuỗi đối xứng (palindrome)
# Nhập chuỗi, kiểm tra có đọc xuôi ngược giống nhau không
# "racecar" → True, "hello" → False
# Gợi ý: So sánh s với s[::-1]
text = input("Nhap chuoi can kiem tra: ")

text_clean = text.lower().replace(" ", "")
is_palindrome = text_clean == text_clean[::-1]
if is_palindrome:
    print(f"'{text}' -> True (La chuoi doi xung)")
else:
    print(f"'{text}' -> False (Khong phai la chuoi doi xung)")