while True:
    try:
        number = int(input("Nhập một số nguyên: "))
        break
    except ValueError:
        print("Số bạn nhập không hợp lệ. Vui lòng nhập lại.")
if number % 2 == 0:
    print(number,' là số chẵn!')
else:
    print(number,' là số lẻ!')