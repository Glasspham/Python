# Viết một chương trình Python để yêu cầu người dùng nhập một số và kiểm tra xem số đó là số chẵn hoặc lẻ
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