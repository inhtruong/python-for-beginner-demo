# Nhập vào số nguyên dương a, nếu a lớn hơn 10 thì ta in ra đây là số lớn hơn 10
a = int(input("Nhập vào số nguyên dương: "))
if a > 10:
    print("Số lớn hơn 10")

#Viết chương trình nhập vào điểm số, in ra kết quả đậu hay rớt dựa trên điểm chuẩn đậu là 5 điểm.
# a = int(input("Nhập vào số nguyên dương: "))
# if a >= 5:
#     print("Chúc mừng bạn đã đậu!")
# else:
#     print("Rất tiếc bạn đã rớt!")


# Viết chương trình tính chiết khấu, với:
# - Nếu amount < 1000 thì không có chiết khấu
# - Nếu 1000 <= amount < 5000 thì chiết khấu 5%
# - Nếu 5000 <= amount < 10000 thì chiết khấu 10%
# - Nếu amount >= 10000 thì chiết khấu 20%

# Sử dụng if-elif-else
# amount = float(input("Nhập vào số tiền: "))
# if amount < 1000:
#     discount = 0
# elif 1000 <= amount < 5000:
#     discount = amount * 5 / 100
# elif 5000 <= amount < 10000:
#     discount = amount * 10 / 100
# else:
#     discount = amount * 20 / 100

# print("Discount:", discount)

# Sử dụng if-else lồng nhau
amount = float(input("Nhập vào số tiền: "))
if amount < 1000:
    discount = 0
else:
    if 1000 <= amount < 5000:
        discount = amount * 5 / 100
    else:
        if 5000 <= amount < 10000:
            discount = amount * 10 / 100
        else:
            discount = amount * 20 / 100

print("Amount:", amount - discount)

# match case 
