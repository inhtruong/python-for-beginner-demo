# # Tạo list trống
# list1 = []
# # Tạo list trống bằng Constructor List()
# list2 = list()
# print(list1)
# print(list2)

# Tạo list có giá trị
# list1 = ["Rohan", "Physics", 21, 69.75]
# list2 = [1, 2, 3, 4, 5]
# list3 = ["a", "b", "c", "d"]
# list4 = [25.50, True, -55, 1+2j]
# print(list1)
# print(list2)
# print(list3)
# print(list4)

# Truy cập các phần tử của List trong Python
# language = ['java', 'python', 'php', 'c++']
# print(language[2])
# print(language[-2])

# Chỉ mục âm
# language = ['java', 'python', 'php', 'c++']
# print(language[-2])

# Phạm vi chỉ mục
# fruits = ["apple", "banana", "guava", "orange", "kiwi", "melon", "mango"]
# print(fruits[2:5])
# print(fruits[:4])
# print(fruits[3:])
# print(fruits[-4:-1])


# Các hoạt động cơ bản trên List
# Kiểm tra sự tồn tại của một Item trong list
# colors = ['red', 'green', 'blue', 'yellow', 'black']
# color = "red"
# if (color in colors):
#     print("\"red\" co ton tai trong list");
# else:
#     print("\"red\" khong ton tai trong list");

# Độ dài của một list trong Python
# colors = ['red', 'green', 'blue', 'yellow', 'black']
# print(len(colors))

# Duyệt các phần tử của một List
# colors = ['red', 'green', 'blue', 'yellow', 'black']
# for color in colors:
#     print(color)

# Thêm phần tử tới List
# colors = ['red', 'green', 'blue', 'yellow', 'black']
# colors.append("orange") # them vao vi tri cuoi cung 
# colors.insert(3, "puple") # tuy chon vi tri them vao
# print(colors)

# Xóa phần tử trong List
# colors = ['red', 'green', 'blue', 'yellow', 'black']
# Xóa chỉ định
# colors.remove("green")
# print(colors)
# # Xóa phần tử cuối cùng hoặc theo index
# colors.pop()
# colors.pop(3)
# print(colors)
# # Xóa toàn bộ phần tử
# colors.clear()
# print(colors) 

# Sắp xếp các phần tử trong List
# colors = ['red', 'green', 'blue', 'yellow', 'black']
# colors.sort()
# print(colors)
# colors.sort(reverse=True)
# print(colors)
# colors.reverse()
# print(colors)

# Nối 2 list trong Python
# colors_1 = ['red', 'green', 'blue']
# colors_2 = ['yellow', 'red']
# colors_3 = colors_1 + colors_2
# print(colors_3)


# Khởi tạo mảng 2 chiều 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Duyệt qua các phần tử
for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    print(matrix[i][j], end=' ') 
  print()