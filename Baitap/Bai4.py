'''
  Viết chương trình nhập vào một chuỗi và in ra số lượng các ký tự số có trong chuỗi đó. 
'''

string = input("Enter a string: ")
count = 0

for i in string:
  if i.isdigit():
    count += 1

print("Number of digits:", count)
