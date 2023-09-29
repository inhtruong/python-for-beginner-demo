'''
  Viết chương trình sắp xếp số dương tăng dần, âm giảm dần. Vị trí tương đối không thay đổi
'''
numbers = []

while True:
    n = input("Nhập một số (nhấn Enter để dừng): ")
    if n == "":
        break
    try:
        n = int(n)  # Chuyển đổi chuỗi nhập thành số nguyên
        numbers.append(n)
    except ValueError:
        print("Không phải là một số nguyên hợp lệ. Vui lòng nhập lại.")

positive = [x for x in numbers if x > 0]
positive.sort()

negative = [x for x in numbers if x < 0]
negative.sort(reverse = True)

result = []
i, j = 0, 0
for num in numbers:
  if num >= 0:
    result.append(positive[i])
    i += 1
  else:
    result.append(negative[j])  
    j += 1

print("List sau khi sắp xếp: ", result)