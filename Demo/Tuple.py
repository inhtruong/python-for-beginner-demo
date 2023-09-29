# # Tạo tuple rỗng
# tuple1 = ()
# print(tuple1)
# # Tạo tuple rỗng bằng Contructor tuple()
# tuple2 = tuple()
# print(tuple2)

# Tạo tuple có giá trị
# tuple1 = ("Rohan", "Physics", 21, 69.75)
# tuple2 = (1, 2, 3, 4, 5)
# tuple3 = ("a", "b", "c", "d")
# tuple4 = (25.50, True, -55, 1+2j)
# print(tuple1)
# print(tuple2)
# print(tuple3)
# print(tuple4)

# Truy cập các phần tử của Tuple trong Python
# language = ('java', 'python', 'php', 'c++')
# print(language[2])
# print(language[-3])

# Chỉ mục âm
# language = ('java', 'python', 'php', 'c++')
# print(language[-3])

# Phạm vi chỉ mục
# fruits = ("apple", "banana", "guava", "orange", "kiwi", "melon", "mango")
# print(fruits[2:5])
# print(fruits[:4])
# print(fruits[3:])
# print(fruits[-4:-1])

# Thay đổi giá trị Tuple
#Khi một tuple được tạo, bạn không thể thay đổi giá trị của nó. Tuple là không thể thay đổi hoặc bất biến.
# Có một cách giải quyết. Đó là bạn có thể chuyển đổi tuple thành một list, thay đổi list và chuyển đổi lại thành tuple.
# x = ("apple", "banana", "cherry")
# print(x)
# y = list(x)
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# Duyệt các giá trị của một Tuple
# colors = ('red', 'green', 'blue', 'yellow', 'black')
# for color in colors:
#     print(color)

# Kiểm tra xem nếu giá trị tồn tại trong Tuple
# fruits = ("apple", "banana", "cherry")
# x = "banana" in fruits
# print(x)

# Nối 2 Tuple trong Python
# colors = ('red', 'green', 'blue')
# numbers = (1, 3)
# tuples = colors + numbers
# print(tuples)
