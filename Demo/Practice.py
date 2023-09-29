

# Nhập danh sách số nguyên từ người dùng
so_nguyen = input("Nhập danh sách số nguyên, cách nhau bằng khoảng trắng: ")

# Chuyển danh sách số nguyên thành mảng
so_nguyen = so_nguyen.split()
list_sort = [];

for i in so_nguyen:
    i = int(i)
    
    # Thêm i vào danh sách
    list_sort.append(i)

list_sort.sort()
print(list_sort)
