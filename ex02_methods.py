"""
Bài tập 02: Phương thức chuỗi 🛠️
===================================
Mục tiêu: Dùng thành thạo các string methods
"""

# TODO 1: Cho email = "  User@Example.COM  "
# Chuẩn hóa email: xóa khoảng trắng, chuyển thường
# In kết quả: "user@example.com"
email = "  User@Example.COM  "
email_clean = email.strip().lower()
print(f"Email sau khi chuan hoa: '{email_clean}'")

# TODO 2: Cho sentence = "hello world python programming"
# a) Chuyển thành Title Case: "Hello World Python Programming"
# b) Đếm số lần chữ "o" xuất hiện
# c) Thay "python" thành "PYTHON"
sentence = "hello world python programming"
sentence_title = sentence.title()
print(f"a) Title Case: {sentence_title}")
count_o = sentence.count("o")
print(f"b) So lan xuat hien cua 'o': {count_o}")
sentence_replaced = sentence.replace("python", "PYTHON")
print(f"c) Sau khi thay the: {sentence_replaced}")

# TODO 3: Nhập họ tên đầy đủ, tách ra họ và tên
# Ví dụ: "Nguyễn Văn An" → Họ: "Nguyễn", Tên: "An"
# Gợi ý: dùng split() và indexing
ho_ten = input("Nhap ho ten day du: ").strip()
cac_tu = ho_ten.split()
if len(cac_tu) >= 2:
    ho = cac_tu[0]     
    ten = cac_tu[-1]     
    print(f"Ho: {ho}")
    print(f"Ten: {ten}")
else:
    print("Vui long nhap day du ca ho va ten!")

# TODO 4: Kiểm tra tên file hợp lệ
# Nhập tên file, kiểm tra có kết thúc bằng .py, .txt, hoặc .csv không
# Gợi ý: dùng endswith()
filename = input("Nhap ten file: ").strip().lower()
duoi_hop_le = (".py", ".txt", ".csv")
if filename.endswith(duoi_hop_le):
    print(f"Tep '{filename}' HOP LE!")
else:
    print(f"Tep '{filename}' KHONG HOP LE! (Phai co duoi .py, .txt, hoac .csv)")

# TODO 5 (Thử thách): Mã hóa Caesar
# Nhập chuỗi và số bước dịch (shift)
# Dịch mỗi ký tự đi shift bước trong bảng chữ cái
# "abc" với shift=3 → "def"
text = input("Nhap chuoi can ma hoa: ")
shift = int(input("Nhap so buoc dich (shift): "))

encrypted_text = ""

for char in text:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')  
        new_char = chr((ord(char) - start + shift) % 26 + start)
        encrypted_text += new_char
    else:
        encrypted_text += char
print(f"Chuoi sau khi ma hoa Caesar: {encrypted_text}")