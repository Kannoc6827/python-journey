import re

# ==========================================
# Mini-project — Text Analyzer
# ==========================================

# Nhập text
text = input("Nhập một đoạn text: ")

# Xử lý text rỗng
if text.strip() == "":
    print("Text rỗng!")
else:
    # ==========================================
    # 1. Chuẩn hóa text
    # ==========================================

    # Xóa khoảng trắng đầu/cuối
    clean_text = text.strip()

    # Chuyển thành chữ thường
    clean_text = clean_text.lower()

    # Tách thành các từ
    words = clean_text.split()

    # Ghép lại bằng một khoảng trắng
    normalized_text = " ".join(words)

    print("\n===== TEXT SAU KHI CHUẨN HÓA =====")
    print(normalized_text)

    # ==========================================
    # 2. Đếm ký tự
    # ==========================================

    character_count = len(normalized_text)

    # ==========================================
    # 3. Đếm từ
    # ==========================================

    word_count = len(words)

    # ==========================================
    # 4. Đếm keyword
    # ==========================================

    keyword = input("\nNhập keyword cần tìm: ")

    keyword = keyword.strip().lower()

    keyword_count = normalized_text.count(keyword)

    # ==========================================
    # 5. Tìm Course Code bằng Regex
    # Ví dụ: PJ-101, PJ-202
    # ==========================================

    course_codes = re.findall(
        r"\b[A-Z]{2}-\d{3}\b",
        text.upper()
    )

    # ==========================================
    # 6. Hiển thị thống kê
    # ==========================================

    print("\n===== THỐNG KÊ =====")

    print("Số ký tự:", character_count)

    print("Số từ:", word_count)

    print(
        f"Số lần keyword '{keyword}' xuất hiện:",
        keyword_count
    )

    print("Course codes:", course_codes)