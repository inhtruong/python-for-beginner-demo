# Hàm kiểm tra số nguyên tố 
def is_prime(number):
  if number < 2:
    return False

  for i in range(2, number):
    if number % i == 0:
      return False
  
  return True

# Hàm liệt kê vị trí số nguyên tố
def find_prime_positions(arr):

  # Khởi tạo mảng lưu kết quả
  positions = []

  # Duyệt mảng đầu vào
  for i in range(len(arr)):

    # Lấy ra phần tử tại vị trí i
    num = arr[i]

    # Kiểm tra có phải số nguyên tố
    if is_prime(num):

      # Thêm vị trí vào kết quả
      positions.append(i)
  
  return positions

# Ví dụ
numbers = [7, 10, 11, 12, 13, 14]
print(find_prime_positions(numbers))

# Kết quả: [0, 2]