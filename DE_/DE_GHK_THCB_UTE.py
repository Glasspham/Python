# Bài 1
# a
chuoi = input("Nhap chuoi ky tu: ")
a, b = map(int, input("Nhap 2 chu so: ").split())
print(chuoi[a:b+1])

# b
print(chuoi[:a] + chuoi[a:b+1].upper() + chuoi[b+1:])

# c
print(chuoi[a+1:b][::-1])


# Bài 2
ho_ten = input("Nhap ho ten: ")
mssv = input("Nhap MSSV: ")
lop = input("Nhap lop: ")
diem = int(input("Nhap diem: "))

print(f"\n{'HO VA TEN':15} | {'MSSV':7} | {'LOP':7} | {'DIEM'}")
print(f"{ho_ten:15} | {mssv:7} | {lop:7} | {diem:1}")

new_diem = float(input("\nNhap diem moi cho sinh vien: "))
diem = new_diem

print("\nSau khi thay doi diem:\n")
print(f"{'HO VA TEN':20} | {'MSSV':7} | {'LOP':7} | {'DIEM'}")
print(f"{ho_ten:20} | {mssv:7} | {lop:7} | {diem:5.2f}")


#Bài 3
numbers = [9, 13, 27, 35, 64, 81, 100]

# a
print("Tổng các chữ số trong list:", sum(numbers))

# b
numbers.sort()
print("Danh sách sau khi sắp xếp:", numbers)

# c
num = int(input("Nhập số mới cần thêm: "))
index = int(input("Nhập vị trí cần thêm (tính từ 0): "))
numbers.insert(index, num)
print(numbers)

# d
k = int(input("Nhập vào vị trí số muốn đổi thành nhị phân: "))
m = bin(numbers[k])[2:]
numbers[k] = m
print(numbers)
