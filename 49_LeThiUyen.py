# student_manager.py

# Danh sách để lưu thông tin các sinh viên.
# Mỗi sinh viên là một dictionary.
student_list = []

def add_student(name, year_of_birth, address):
    """
    YÊU CẦU 1: Hoàn thiện hàm này.
    - Tạo một dictionary để lưu thông tin sinh viên.
    - Thêm dictionary đó vào danh sách `student_list`.
    - In ra thông báo "Da them sinh  vien <ten> thanh cong."
    """
    ### VIẾT CODE CỦA BẠN VÀO ĐÂY ###
    student = {
        "name": name,
        "year_of_birth": year_of_birth,
        "address": address
    }
    student_list.append(student)
    print(f"Da them sinh vien {name} thanh cong.")

def print_student_list():
    """
    YÊU CẦU 2: Hoàn thiện hàm này.
    - In ra tiêu đề "--- DANH SACH SINH VIEN ---".
    - Nếu danh sách trống, in ra "Danh sach trong.".
    - Nếu không, duyệt qua `student_list` và in thông tin mỗi sinh viên
      trên một dòng theo định dạng: " - Ten: [Họ tên], Nam sinh: [Năm sinh], Dia chi: [Địa chỉ]"
    """
    ### VIẾT CODE CỦA BẠN VÀO ĐÂY ###
    print("--- DANH SACH SINH VIEN ---")
    if not student_list:
        print("Danh sach trong.")
    else:
        for s in student_list:
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")
    
def search_student(search_name):
    """
    YÊU CẦU 3: Hoàn thiện hàm này.
    - In ra tiêu đề "--- KET QUA TIM KIEM ---".
    - Tìm kiếm trong `student_list` tất cả các sinh viên có tên (không phân biệt hoa thường)
      chứa `search_name`.
    - In ra thông tin của các sinh viên tìm thấy (theo định dạng như hàm print_student_list).
    - Nếu không tìm thấy, in ra "Khong tim thay sinh vien nao.".
    """
    ### VIẾT CODE CỦA BẠN VÀO ĐÂY ###
    print("--- KET QUA TIM KIEM ---")
    found = False
    for s in student_list:
        if search_name.lower() in s["name"].lower():
            print(f" - Ten: {s['name']}, Nam sinh: {s['year_of_birth']}, Dia chi: {s['address']}")
            found = True
    if not found:
        print("Khong tim thay sinh vien nao.")