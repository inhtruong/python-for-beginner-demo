# # Tạo Set rỗng
# set1 = {}
# # Tạo Set rỗng bằng Contructor set()
# set2 = set() #
# print(set1)
# print(set2)

# # Tạo Set có giá trị
# set1 = {"Rohan", "Physics", 21, 69.75}
# set2 = {1, 2, 3, 4, 5}
# set3 = {"c", "d", "c", "d"}
# set4 = {25.50, True, -55, 1+2j}
# print(set1)
# print(set2)
# print(set3)
# print(set4)

# Truy cập các phần tử của Set trong Python
# languages = {"java", "python", "php", "c++"}
# for language in languages:
#     print(language)

# Kiểm tra tồn tại trong Set
# languages = {"java", "python", "php", "c++"}
# print("python" in languages)

# # Các thao tác cơ bản trong Set
# # Thêm phần tử vào Set
# languages = {"java", "python", "php", "c++"}
# languages.add("java") # them 1 phan tu
# languages.update(["python", "c"]) # them nhieu phan tu
# print(languages)

# # Xóa phần tử trong Set
# languages = {"java", "python", "php", "c++"}
# # # Nếu phần tử cần xóa không tồn tại, hàm remove() sẽ phát sinh lỗi.
# languages.remove("python")
# print(languages)
# # # Nếu mục cần xóa không tồn tại, discard() sẽ không sinh ra lỗi.
# languages.discard("c++")
# print(languages)
# languages.pop()
# languages.clear()

# # Độ dài của Set
# languages = {"java", "python", "php", "c++"}
# print(len(languages))

# TODO:
#Phép toán: union(), intersection()
#Kiểm tra: issubset(), issuperset()

