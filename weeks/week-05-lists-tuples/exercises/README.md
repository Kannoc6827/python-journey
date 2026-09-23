# Tuần 05 — Bài tập List & Tuple 📋

> **Python Journey** — Các bài tập thực hành tuần 05: List, Tuple, Slicing, Unpacking

## 📂 Các bài tập

| File | Chủ đề | Độ khó |
|:-----|:-------|:-------|
| `ex01_lists.py` | Tạo và thao tác List | 🟢 Dễ |
| `ex02_slicing.py` | Slicing & List Comprehension | 🟢 Dễ |
| `ex03_tuples.py` | Tuple & Unpacking | 🟡 Trung bình |

---

## 📝 Bài 01 — Tạo và thao tác List (`ex01_lists.py`)

### Mục tiêu
Thành thạo CRUD (Create, Read, Update, Delete) trên list.

### Nội dung bài tập

**TODO 1** — Tạo list 5 môn học, dùng `append()` thêm, `insert()` chèn, `remove()` xóa.

**TODO 2** — Sắp xếp list điểm, tìm max/min/avg, đếm điểm đạt.

**TODO 3** — Nhập n số từ người dùng, tính tổng/trung bình/min/max.

**TODO 4** — Lọc phần tử trùng lặp khỏi list (không dùng `set`).

### Khái niệm chính

| Phương thức | Tác dụng | Ví dụ |
|:-----------|:---------|:------|
| `append(x)` | Thêm `x` vào cuối list | `fruits.append("mango")` |
| `insert(i, x)` | Chèn `x` vào vị trí `i` | `list.insert(0, "first")` |
| `remove(x)` | Xóa phần tử đầu tiên có giá trị `x` | `list.remove("apple")` |
| `pop()` | Xóa và trả về phần tử cuối | `last = list.pop()` |
| `sort()` | Sắp xếp tại chỗ | `nums.sort()` |
| `sorted(lst)` | Trả về list mới đã sắp xếp | `new = sorted(nums)` |

### Lưu ý
- `append()` nhanh hơn `insert()` — ưu tiên dùng `append()` khi có thể.
- `sort()` thay đổi trực tiếp list gốc; `sorted()` trả về list mới.
- Khi lọc trùng lặp không dùng `set`, hãy dùng list phụ + kiểm tra `if item not in unique_list`.

---

## 📝 Bài 02 — Slicing & List Comprehension (`ex02_slicing.py`)

### Mục tiêu
Nắm vững slicing và viết list comprehension Pythonic.

### Nội dung bài tập

**TODO 1** — Slicing: lấy 5 số đầu, 5 số cuối, các số ở chỉ số chẵn từ list 1-20.

**TODO 2** — List comprehension cơ bản: bình phương, số chẵn, in hoa.

**TODO 3** — Lọc với comprehension: điểm đạt/rớt, gán nhãn.

**TODO 4** — Ma trận chuyển vị (transpose).

### Cú pháp Slicing

```python
lst[start:stop:step]
```

| Biểu thức | Ý nghĩa |
|:----------|:--------|
| `lst[:n]` | n phần tử đầu |
| `lst[-n:]` | n phần tử cuối |
| `lst[::2]` | Mỗi 2 phần tử (chỉ số chẵn) |
| `lst[::-1]` | Đảo ngược list |

### List Pattern

```python
# Cơ bản
[kết_quả for biến in iterable]

# Có điều kiện
[kết_quả for biến in iterable if điều_kiện]

# Có điều kiện + biến đổi
[giá_trị_mới if điều_kiện else giá_trị_khác for biến in iterable]
```

### Lưu ý
- List comprehension ngắn gọn hơn `for` loop nhưng không nên lạm dụng.
- Ma trận chuyển vị `[[row[i] for row in matrix] for i in range(cols)]` là pattern hay gặp.

---

## 📝 Bài 03 — Tuple & Unpacking (`ex03_tuples.py`)

### Mục tiêu
Hiểu tuple, immutability, unpacking, và kết hợp với hàm.

### Nội dung bài tập

**TODO 1** — Gán biến từ tuple qua unpacking. Thử gán lại → lỗi `TypeError`.

**TODO 2** — Hàm trả về tuple, unpack kết quả thành nhiều biến.

**TODO 3** — Danh sách sinh viên (list tuple): duyệt, tìm max, sắp xếp.

**TODO 4** — Kết hợp `enumerate()` + `zip()` để duyệt song song có thứ tự.

### Khái niệm chính

```python
# Tuple tạo bằng dấu ngoặc tròn
coord = (3, 7)

# Unpacking
x, y = coord  # x=3, y=7

# Tuple là IMMUTABLE — không thể thay đổi
# coord[0] = 10  # ❌ TypeError!

# Hàm trả về nhiều giá trị = trả về tuple
def get_stats():
    return 1, 2, 3  # thực chất return (1, 2, 3)

a, b, c = get_stats()
```

### Lưu ý
- Tuple dùng khi dữ liệu **không nên thay đổi** (tọa độ, cấu hình, bản ghi cố định).
- Unpacking giúp code rõ ràng hơn: `name, score = student` thay vì `student[0], student[1]`.
- `enumerate(zip(names, scores), start=1)` = vừa có thứ tự vừa ghép cặp.

---

## 🖥️ Cách chạy

> ⚠️ Trên Windows PowerShell, cần đổi encoding để hiển thị tiếng Việt:
> ```powershell
> $env:PYTHONUTF8=1; python weeks\week-05-lists-tuples\exercises\ex01_lists.py
> ```
> Hoặc dùng `chcp 65001` trước khi chạy.

### Chạy tuần tự (không cần input)
```bash
python weeks/week-05-lists-tuples/exercises/ex02_slicing.py
python weeks/week-05-lists-tuples/exercises/ex03_tuples.py
```

### Chạy file cần input
```bash
python weeks/week-05-lists-tuples/exercises/ex01_lists.py
```
File này yêu cầu nhập `n` và `n` số từ bàn phím.

---

## 📊 So sánh Mutable vs Immutable

| Đặc điểm | List `[]` | Tuple `()` |
|:---------|:----------|:-----------|
| Có thể thay đổi | ✅ Có | ❌ Không |
| Cú pháp | `[1, 2]` | `(1, 2)` |
| Dùng khi | Dữ liệu thay đổi | Dữ liệu cố định |
| Hiệu suất | Chậm hơn (dynamic) | Nhanh hơn (fixed) |
| Làm dict key | ❌ Không | ✅ Có |

---

## 🔑 Ghi nhớ tuần này

> 1. **List mutable** — append/insert/remove/sort thay đổi trực tiếp
> 2. **Tuple immutable** — an toàn hơn, nhanh hơn, dùng khi dữ liệu cố định
> 3. **Unpacking** — gán giá trị từ iterable vào nhiều biến cùng lúc
> 4. **Slicing** — `start:stop:step` linh hoạt cắt list
> 5. **Comprehension** — viết nhanh, đọc rõ, không lạm dụng
