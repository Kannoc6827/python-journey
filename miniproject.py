
n = int(input("Nhập số lượng môn học: "))

subjects = []
total_points = 0
total_credits = 0


for i in range(n):
    print(f"\n--- Môn {i + 1} ---")

    name = input("Tên môn: ")
    credits = int(input("Số tín chỉ: "))
    score_10 = float(input("Điểm (0-10): "))


    while score_10 < 0 or score_10 > 10:
        print("Điểm phải từ 0 đến 10!")
        score_10 = float(input("Nhập lại điểm: "))

  
    score_4 = score_10 * 4 / 10


    subjects.append([name, credits, score_10, score_4])

    total_points += score_4 * credits
    total_credits += credits

gpa = total_points / total_credits


if gpa >= 3.6:
    rank = "Xuất sắc"
elif gpa >= 3.2:
    rank = "Giỏi"
elif gpa >= 2.5:
    rank = "Khá"
elif gpa >= 2.0:
    rank = "Trung bình"
else:
    rank = "Không đạt"

print("\n" + "=" * 65)
print("                 BẢNG KẾT QUẢ GPA")
print("=" * 65)

print(f"{'Môn học':<25}{'TC':<8}{'Điểm 10':<12}{'Điểm 4':<10}")
print("-" * 65)

for subject in subjects:
    print(f"{subject[0]:<25}{subject[1]:<8}{subject[2]:<12.2f}{subject[3]:<10.2f}")

print("-" * 65)
print(f"Tổng tín chỉ: {total_credits}")
print(f"GPA: {gpa:.2f}")
print(f"Xếp loại: {rank}")
print("=" * 65)