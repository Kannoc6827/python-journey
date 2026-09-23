"""
Bài tập 01: Tạo và thao tác List 📋
=====================================
Mục tiêu: Thành thạo CRUD trên list
"""

# TODO 1: Tạo list 5 môn học yêu thích
subjects = ["Toán", "Văn", "Anh", "Lý", "Hóa"]
print("Ban đầu:", subjects)

# Thêm 1 môn bằng append()
subjects.append("Tin học")
print("Sau khi append:", subjects)

# Chèn 1 môn vào vị trí 2 bằng insert()
subjects.insert(2, "Sinh học")
print("Sau khi insert:", subjects)

# Xóa 1 môn bằng remove()
subjects.remove("Văn")
print("Sau khi remove:", subjects)


# TODO 2: Thao tác trên list diem
diem = [7, 9, 5, 8, 10, 6, 4, 9]

# a) Sắp xếp tăng dần (tại chỗ)
diem.sort()
print("\nSắp xếp tăng dần:", diem)

# b) Tìm điểm cao nhất, thấp nhất, trung bình
max_diem = max(diem)
min_diem = min(diem)
avg_diem = sum(diem) / len(diem)
print(f"Cao nhất: {max_diem}, Thấp nhất: {min_diem}, Trung bình: {avg_diem:.2f}")

# c) Đếm số điểm >= 5 (đạt)
so_dat = sum(1 for d in diem if d >= 5)
print("Số điểm đạt (>= 5):", so_dat)


# TODO 3: Nhập n số từ người dùng, lưu vào list
n = int(input("\nNhập số lượng phần tử n: "))
user_nums = []
for i in range(n):
    val = float(input(f"Nhập số thứ {i+1}: "))
    user_nums.append(val)

if user_nums:
    print(f"Tổng: {sum(user_nums)}")
    print(f"Trung bình: {sum(user_nums) / len(user_nums):.2f}")
    print(f"Min: {min(user_nums)}, Max: {max(user_nums)}")


# TODO 4 (Thử thách): Xóa phần tử trùng lặp khỏi list (giữ thứ tự, KHÔNG dùng set)
nums = [1, 3, 2, 3, 1, 5, 2, 4]
unique_nums = []
for item in nums:
    if item not in unique_nums:
        unique_nums.append(item)

print("\nList sau khi lọc trùng:", unique_nums)