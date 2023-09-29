# Tạo Dictionary trống
dict1 = {}
# Tạo Dictionary rỗng bằng Contruction Dict()
dict2 = dict()
print(dict1)
print(dict2)

# Tạo Dictionary có giá trị
# dictStudent = {"name": "Rohan", "age": 21, "gender": "Male"}
# print(dictStudent)

# Truy cập các phần tử của Dictionary trong Python
# dictLanguage = {"java": "Java", "python": "Python", "php": "PHP", "c++": "C++"}
# print(dictLanguage["c++"])
# print(dictLanguage.get("java"))

# Thay đổi giá trị của một Dictionary trong Python
# dictStudent = {"name": "Rohan", "age": 21, "gender": "Male"}
# dictStudent["age"] = 25
# print(dictStudent)

# Duyệt các item của Dictionary trong Python
# dictStudent = {"name": "Rohan", "age": 21, "gender": "Male"}
# for key in dictStudent:
#     print(key, ":", dictStudent[key])

# Kiểm tra nếu key tồn tại
# dictCar = {
#     "brand": "Honda",
#     "model": "Honda Civic",
#     "year": 1972
# }
# str1 = "model"
# if str1 in dictCar:
#     print("Khoa \"model\" co ton tai.", dictCar[str1])
# else:
#     print("Khoa \"model\" khong ton tai.")

# Độ dài của Dictionary
# dictStudent = {"name": "Rohan", "age": 21, "gender": "Male"}
# print(len(dictStudent))

# Thêm một phần tử vào Dictionary
# dictStudent = {"name": "Rohan", "age": 21, "gender": "Male"}
# dictStudent["address"] = "Huế"
# print(dictStudent)

# # Xóa một phần tử trong Dictionary
# dictStudent = {"name": "Rohan", "age": 21, "gender": "Male"}
# # Hàm pop() xóa item với key được chỉ định
# dictStudent.pop("age")
# print(dictStudent)
# # Hàm popitem() xóa phần tử cuối cùng
# dictStudent.popitem()
# print(dictStudent)
# # Hàm clear() xóa toàn bộ phần tử
# dictStudent.clear()
# print(dictStudent)

# Copy Dictionary
# dictStudent = {"name": "Rohan", "age": 21, "gender": "Male"}
# dictAssign = dictStudent
# dictCopy = dictStudent.copy()

# dictStudent["address"] = "Huế"

# print(dictAssign)
# print(dictCopy)

# Dictionary lồng nhau
# myClass = {
#   "student1" : {
#     "name" : "Van",
#     "birthday" : 2004
#   },
#   "student2" : {
#     "name" : "Minh",
#     "birthday" : 2007
#   },
#   "student3" : {
#     "name" : "Phuc",
#     "birthday" : 2011
#   }
# }
# print(myClass)
