"""
Bài tập 03: Tuple & Unpacking 📦
==================================
Mục tiêu: Hiểu tuple và khi nào dùng
"""

# TODO 1: Tuple & Unpacking
coord = (3, 7)
x, y = coord
print(f"x = {x}, y = {y}")

# Thử gán lại giá trị cho tuple:
# coord[0] = 10 
# Lỗi sẽ xảy ra: TypeError: 'tuple' object does not support item assignment
# Nguyên nhân: Tuple là kiểu dữ liệu immutable (không thể thay đổi sau khi khởi tạo).


# TODO 2: Hàm trả về tuple
def tinh_thong_ke(numbers):
    if not numbers:
        return None, None, None
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

# Gọi hàm và unpack kết quả
sample_list = [12, 45, 2, 67, 34, 89, 23]
min_val, max_val, avg_val = tinh_thong_ke(sample_list)
print(f"\nThống kê -> Min: {min_val}, Max: {max_val}, Trung bình: {avg_val:.2f}")


# TODO 3: Danh sách sinh viên
students = [("An", 8.5), ("Bình", 7.0), ("Châu", 9.2), ("Dũng", 6.5)]

# a) In ra tên và điểm mỗi sinh viên bằng unpacking
print("\nDanh sách sinh viên:")
for name, score in students:
    print(f"- {name}: {score} điểm")

# b) Tìm sinh viên có điểm cao nhất
top_student = max(students, key=lambda student: student[1])
print(f"\nSinh viên điểm cao nhất: {top_student[0]} ({top_student[1]} điểm)")

# c) Sắp xếp theo điểm giảm dần
sorted_students = sorted(students, key=lambda student: student[1], reverse=True)
print("Danh sách sắp xếp giảm dần theo điểm:", sorted_students)


# TODO 4 (Thử thách): Combine enumerate & zip
names = ["A", "B", "C"]
scores = [8, 9, 7]

print("\nKết quả hiển thị:")
for idx, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{idx}. {name} — {score} điểm")
