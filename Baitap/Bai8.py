'''
  Đếm số lượng giá trị tận cùng bằng 5 trong mảng
'''

# Hàm kiểm tra kết thúc bằng 5
def ends_with_5(num):
  return num % 10 == 5

# Hàm đếm số lượng tận cùng bằng 5
def count_ends_with_5(arr):

  # Khởi tạo đếm 
  count = 0

  # Duyệt mảng
  for value in arr:

    # Ep kiểu về số nguyên để lấy chữ số cuối cùng
    num = int(value)

    # Kiểm tra có kết thúc bằng 5
    if ends_with_5(num):
      count += 1

  return count

# Ví dụ 
numbers = [15, 17, 25, 5, 30, 23, 145]
print(count_ends_with_5(numbers))

# Kết quả: 3