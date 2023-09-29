'''
  Viết chương trình nhập vào một list số nguyên, sau đó sắp xếp lại list đó theo thứ tự tăng dần và in ra màn hình.
'''
# Nhập dữ liệu
nums = []
n = int(input("Nhập số phần tử của list: "))
for i in range(n):
    x = int(input("Nhập số nguyên thứ %d: " % (i+1)))
    nums.append(x)

# Sắp xếp list  
nums.sort()

print("List sau khi sắp xếp: ", nums)


# Sử dụng vòng lặp for

# Nhập dữ liệu
nums = []
n = int(input("Nhập số phần tử của list: "))
for i in range(n):
    x = int(input("Nhập số nguyên thứ %d: " % (i+1)))
    nums.append(x)

# Sắp xếp bằng vòng lặp 
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

print("List sau khi sắp xếp: ", nums)