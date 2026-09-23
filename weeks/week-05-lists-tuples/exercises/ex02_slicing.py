"""
Bài tập 02: Slicing & List Comprehension ✂️
=============================================
Mục tiêu: Cắt list và viết comprehension
"""

# TODO 1: Slicing
numbers = list(range(1, 21))

head_5 = numbers[:5]          # 5 số đầu
tail_5 = numbers[-5:]         # 5 số cuối
even_positions = numbers[::2] # Vị trí chỉ số chẵn (index 0, 2, 4...)

print("5 số đầu:", head_5)
print("5 số cuối:", tail_5)
print("Các số ở chỉ số chẵn:", even_positions)


# TODO 2: List comprehension cơ bản
# a) List bình phương từ 1 đến 10
squares = [x**2 for x in range(1, 11)]
print("\nBình phương (1-10):", squares)

# b) List số chẵn từ 0 đến 20
evens = [x for x in range(0, 21) if x % 2 == 0]
print("Số chẵn (0-20):", evens)

# c) Chuyển thành in hoa
words = ["hello", "world", "python"]
uppercase_words = [w.upper() for w in words]
print("Chữ in hoa:", uppercase_words)


# TODO 3: Lọc với comprehension
scores = [45, 78, 92, 56, 33, 88, 71, 95, 62, 50]

# a) Điểm >= 60
pass_scores = [s for s in scores if s >= 60]
# b) Điểm < 50
fail_scores = [s for s in scores if s < 50]
# c) Gán nhãn Đạt/Rớt
results = ["Đạt" if s >= 50 else "Rớt" for s in scores]

print("\nĐiểm >= 60:", pass_scores)
print("Điểm < 50:", fail_scores)
print("Kết quả đánh giá:", results)


# TODO 4 (Thử thách): Ma trận chuyển vị
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("\nMa trận chuyển vị:", transpose)
