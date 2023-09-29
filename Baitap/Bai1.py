'''
  Viết chương trình tạo một dictionary gồm các key là tên sinh viên và value là điểm số của sinh viên đó, sau đó in ra dictionary vừa tạo.
'''

# Khởi tạo dict rỗng
scores = {}

# Nhập số lượng sinh viên
n = int(input("Nhập số lượng sinh viên: "))

# Nhập thông tin từng sinh viên
for i in range(n):
    name = input("Nhập tên sinh viên: ")
    score = float(input("Nhập điểm sinh viên: "))
    
    # Thêm vào dict
    scores[name] = score

# In ra kết quả   
print(scores)