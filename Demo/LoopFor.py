# Sử dụng "for" với String
# str1 = '''
# Beautiful is better than ugly.
# Explicit is better than implicit.
# '''
# for char in str1:
#     if char not in 'aeiou':
#         print (char, end='')

# Sử dụng "for" với Tuple
# numbers = (34,54,67,21,78,97,45,44,80,19)
# total = 0
# for num in numbers:
#   total += num    # total = total + num

# print ("Total =", total)


# Sử dụng "for" với List
# numbers = [34,54,67,21,78,97,45,44,80,19]
# total = 0
# for num in numbers:
#    if num%2 == 0:
#       print (num)

# "for" với object range
# phạm vi được tạo từ 10 đến 19 tăng dần
# numbers = range(10,20, 2)
# print (list(numbers))

# phạm vi được tạo từ 1 đến 10 tăng dần theo bước 2
# numbers = range(1, 10, 2)
# print (list(numbers))

# Sử dụng else trong vòng lặp for
# numbers = [1, 2, 5, 7, 9]
# found = False

# for number in numbers:
#   if number % 2 == 0:
#     print(number, "is even")
#     found = True
# else:
#   print("No even number found")
  