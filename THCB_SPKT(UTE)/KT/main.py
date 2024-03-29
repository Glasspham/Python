# Bai 1
a = int(input("Enter a number: "))
for i in range(a+1):
    f = True
    if i < 2:
        f = False
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            f = False
    if f:
        print(i)



# Bai 2
lst = list(map(int, input().split()))
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(lst)



# Bai 3
s = (str(i) for i in input().split())
for i in s:
    print(i, end=" ")



# Bai 4
huong_dang_dung = input("Nhập hướng đang đứng (Đông/Tây/Nam/Bắc): ")
chuoi_xoay = input("Nhập chuỗi lệnh xoay (vd: T400 P5555 T2 P91): ").split()
for lenh in chuoi_xoay:
    huong_xoay = lenh[0]
    so_lan_xoay = int(lenh[1:])
    if huong_xoay == 'T':
        for _ in range(so_lan_xoay):
            if huong_dang_dung == 'Đông':
                huong_dang_dung = 'Bắc'
            elif huong_dang_dung == 'Bắc':
                huong_dang_dung = 'Tây'
            elif huong_dang_dung == 'Tây':
                huong_dang_dung = 'Nam'
            elif huong_dang_dung == 'Nam':
                huong_dang_dung = 'Đông'
    elif huong_xoay == 'P':
        for _ in range(so_lan_xoay):
            if huong_dang_dung == 'Đông':
                huong_dang_dung = 'Nam'
            elif huong_dang_dung == 'Nam':
                huong_dang_dung = 'Bắc'
            elif huong_dang_dung == 'Bắc':
                huong_dang_dung = 'Tây'
            elif huong_dang_dung == 'Tây':
                huong_dang_dung = 'Đông'
print("Hướng đang đứng sau khi thực hiện lệnh là:", huong_dang_dung)



# Bai 5
s  = input("Nhập chuỗi: ")
num = 0
for i in s:
    if i.isdigit():
        num = num * 10 + int(i)
    else:
        for _ in range(num):
            print(i, end="")
        num = 0



# Bai 6
s = input("Nhập chuỗi: ")
sum = 0 
for i in s:
    sum += int(i)
print(sum)



# Bai 7
A = list(map(int, input("Nhập list 13 phần tử số nguyên: ").split()))
max_length = 1
current_length = 1
end_index = 0
for i in range(1, len(A)):
    if A[i] > A[i - 1]:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            end_index = i - 1
        current_length = 1
if current_length > max_length:
    max_length = current_length
    end_index = len(A) - 1
B = []
for i in range(end_index - max_length + 1, end_index + 1):
    B.append(A[i])
print("List con dài nhất tăng liên tiếp là:", B)


    
# Bai 8
giay = int(input("Nhap so giay: "))
ngay = giay // 86400
giay %= 86400
gio = giay // 3600
giay %= 3600
phut = giay // 60
giay %= 60
print(f"{ngay}:{gio}:{phut}:{giay}")



# Bai 9
n = int(input("Nhập số nguyên dương n: "))
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    f1 = 0
    f2 = 1
    for i in range(2, n + 1):
        f1, f2 = f2, f1 + f2
    print(f2)