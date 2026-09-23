# Tuần 06 — Bài tập Vòng lặp 🔁

> **Python Journey** — Các bài tập thực hành tuần 06: For, While, Nested Loops, enumerate, zip

## 📂 Các bài tập

| File | Chủ đề | Độ khó |
|:-----|:-------|:-------|
| `ex01_for_loop.py` | Vòng lặp for cơ bản | 🟢 Dễ |
| `ex02_while_loop.py` | Vòng lặp while + nhập liệu | 🟡 Trung bình |
| `ex03_patterns.py` | In hoa văn với nested loop | 🟠 Khó |

---

## 📝 Bài 01 — Vòng lặp for (`ex01_for_loop.py`)

### Mục tiêu
Dùng `for` để duyệt list, `range()`, `enumerate()`, `zip()`.

### Nội dung bài tập

**TODO 1** — Nhập số `n`, in bảng cửu chương từ 1 đến 10.

**TODO 2** — Duyệt list `fruits` và in kèm số thứ tự bằng `enumerate()`.

**TODO 3** — Ghép cặp 2 list `names` và `scores` bằng `zip()`, in `"Tên: điểm"`.

**TODO 4** — Tính tổng số chẵn từ 1 đến 100 bằng `for` + `range`.

**TODO 5** *(Thử thách)* — In `n` số Fibonacci đầu tiên (nhập từ bàn phím).

### Khái niệm chính

```python
# for duyệt list
for item in ["a", "b", "c"]:
    print(item)

# for duyệt range
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8
    print(i)
```

### enumerate() — Số thứ tự

```python
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")
# 1. apple
# 2. banana
# 3. cherry
```

> Khi cần đánh số, **dùng `enumerate()`** thay vì quản lý biến đếm thủ công.

### zip() — Duyệt song song

```python
names = ["An", "Bình"]
scores = [8, 9]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

> `zip()` ghép cặp các iterable song song. Dùng khi cần duyệt nhiều list cùng lúc.

### Fibonacci Pattern

```python
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
# 0 1 1 2 3 5 8 13 21 ...
```

> **Unpacking nhiều biến**: `a, b = b, a + b` tính đồng thời (không cần temp variable).

---

## 📝 Bài 02 — Vòng lặp while (`ex02_while_loop.py`)

### Mục tiêu
Dùng `while` khi không biết trước số lần lặp. Xử lý nhập liệu an toàn.

### Nội dung bài tập

**TODO 1** — Đếm ngược 10 → 1, in "Phóng! 🚀".

**TODO 2** — Trò chơi đoán số (random 1-100), gợi ý cao/thấp, đếm số lần.

**TODO 3** — Nhập tuổi lặp lại cho đến khi hợp lệ (1-120) bằng `while True + break`.

**TODO 4** *(Thử thách)* — Menu tính toán: cộng/trừ/nhân/thoát, lặp đến khi chọn thoát.

### Khái niệm chính

```python
# while cơ bản
i = 10
while i >= 1:
    print(i)
    i -= 1  # ⚠️ BẮT BUỘC phải có cơ chế thoát!
```

> ⚠️ **Cảnh báo**: Nếu quên cập nhật biến điều kiện → **vòng lặp vô hạn** → treo máy!

### while True + break — Nhập liệu an toàn

```python
while True:
    value = input("Nhập: ")
    if hợp_lệ:
        break  # thoát khỏi vòng lặp
    print("Thử lại!")
```

> Đây là **pattern tiêu chuẩn** để yêu cầu nhập liệu hợp lệ trong Python.

### break vs continue

| Từ khóa | Tác dụng |
|:--------|:---------|
| `break` | Thoát **ngay** khỏi vòng lặp |
| `continue` | Bỏ qua iteration hiện tại, chuyển iteration tiếp theo |

---

## 📝 Bài 03 — In hoa văn với Nested Loops (`ex03_patterns.py`)

### Mục tiêu
Thành thạo vòng lặp lồng nhau để in các hoa văn hình học.

### Nội dung bài tập

**TODO 1** — Tam giác vuông cao `n` dòng.

**TODO 2** — Tam giác cân (căn giữa) cao `n` dòng.

**TODO 3** — Kim cương cao `n` dòng (n lẻ).

**TODO 4** *(Thử thách)* — Bàn cờ `n × n`.

### Pattern cốt lõi

Mỗi bài in hoa văn đều theo cùng logic:
1. **Vòng ngoài**: duyệt hàng (dòng)
2. **Vòng trong hoặc phép tính**: xác định nội dung mỗi cột
3. **`print()` cuối dòng**: xuống dòng sau mỗi hàng

### Giải thích từng bài

**Tam giác vuông** — hàng `i` có `i` dấu `*`:
```python
for i in range(1, n + 1):
    print("*" * i)
```

**Tam giác cân** — hàng `i` có `(n-i)` khoảng trắng + `(2i-1)` dấu `*`:
```python
for i in range(1, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)
```

**Kim cương** = tam giác cân trên + tam giác cân dưới (đảo ngược, bỏ dòng giữa):
```python
# Phần trên
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
# Phần dưới (lùi lại)
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
```

**Bàn cờ** — ô `(r, c)` đen/trắng theo `(r+c) % 2`:
```python
for r in range(n):
    for c in range(n):
        if (r + c) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()
```

### Lưu ý
- Với các hoa văn có căn giữa, hãy tính: `số khoảng trắng = n - dòng_hiện_tại`.
- `range(a, b, -1)` để lùi ngược.
- `end=" "` để in cùng dòng (không xuống dòng tự động).

---

## 🖥️ Cách chạy

> ⚠️ Trên Windows PowerShell, cần đổi encoding để hiển thị tiếng Việt:
> ```powershell
> $env:PYTHONUTF8=1; python weeks\week-06-loops\exercises\ex01_for_loop.py
> ```

### Chạy tuần tự
```bash
python weeks/week-06-loops/exercises/ex01_for_loop.py
python weeks/week-06-loops/exercises/ex02_while_loop.py
python weeks/week-06-loops/exercises/ex03_patterns.py
```

### Chạy ngược (kiểm tra)
```bash
# Chạy solution trước nếu bí:
python weeks/week-06-loops/solutions/ex01_for_loop_sol.py
```

---

## 🔑 Ghi nhớ tuần này

> 1. **`for`** — dùng khi biết trước số lần lặp (duyệt list, range)
> 2. **`while`** — dùng khi không biết trước (nhập liệu, chờ điều kiện)
> 3. **`break`** — thoát loop; **`continue`** — bỏ qua iteration
> 4. **`while True + break`** — pattern chuẩn cho nhập liệu hợp lệ
> 5. **`enumerate()`** — cần số thứ tự khi duyệt list
> 6. **`zip()`** — duyệt song song nhiều list
> 7. **Nested loop** — in hoa văn: vòng ngoài = hàng, vòng trong = cột
