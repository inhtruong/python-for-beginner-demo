'''
  Hãy liệt kê các giá trị có toàn chữ số lẻ trong mảng 1 chiều các số nguyên
'''

def find_odd_digits(numbers):

  # Khởi tạo mảng lưu kết quả 
  odd_numbers = []

  # Duyệt qua từng phần tử trong mảng đầu vào
  for number in numbers:

    # Chuyển số sang dạng chuỗi
    string_number = str(abs(number))

    # Giả sử ban đầu là số có toàn chữ số lẻ
    is_odd = True

    # Duyệt qua từng chữ số
    for digit in string_number:
      
      # Chuyển chữ số sang kiểu int
      int_digit = int(digit)

      # Nếu chữ số chia hết cho 2 thì không phải lẻ
      if int_digit % 2 == 0:
        is_odd = False
        break
    
    # Nếu vẫn là số lẻ thì thêm vào kết quả
    if is_odd:
      odd_numbers.append(number)

  return odd_numbers

numbers = [123, 455, 345, 7890, -13579, 24680]
print(find_odd_digits(numbers))

# Kết quả [-13579]