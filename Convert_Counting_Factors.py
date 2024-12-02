def DECtoBIN(num, precision):
    binary = "0."

    while num > 0 and precision > 0:
        num *= 2
        if num >= 1:
            binary += '1'
            num -= 1
        else:
            binary += '0'
        precision -= 1

    return binary

select = int(input("Bạn cần chuyển gì:\n"
                   " 1. Từ DEC sang BIN.\n"
                   " 2. Từ DEC sang OCT.\n"
                   " 3. Từ DEC sang HEX.\n"
                   " 4. Từ BIN sang DEC.\n"
                   " 5. Từ BIN sang OCT.\n"
                   " 6. Từ BIN sang HEX.\n"
                   " 7. Từ OCT sang DEC.\n"
                   " 8. Từ OCT sang BIN.\n"
                   " 9. Từ OCT sang HEX.\n"
                   "10. Từ HEX sang DEC.\n"
                   "11. Từ HEX sang BIN.\n"
                   "12. Từ HEX sang OCT.\n"
                   "=========================\n"
                   "Nhập số của chức năng: "))

if select == 1:
    select_1 = int(input("Từ DEC sang BIN!\n"
                         "Có 2 lựa chọn:\n"
                         "1. Số tự nhiên.\n"
                         "2. Số thuộc khoảng (0;1).\n"
                         "=========================\n"
                         "Nhập số của chức năng: "))
    
    if select_1 == 1:
        decimalNumber = int(input("Nhập số tự nhiên: "))
        binaryNumber = bin(decimalNumber)[2:]
        print(f"Số nhị phân tương ứng của {decimalNumber} là {binaryNumber}")

    elif select_1 == 2:
        decimalNumber = float(input("Nhập số thuộc khoảng (0;1): "))
        precision = 8
        print(f"Số nhị phân sắp xếp của {decimalNumber} là {DECtoBIN(decimalNumber, precision)}")

elif select == 2:
    decimalNumber = int(input("Từ DEC sang OCT!\nNhập dãy số vào: "))
    octalNumber = oct(decimalNumber)[2:]
    print(f"Hệ cơ số 8 tương ứng của {decimalNumber} là {octalNumber}")

elif select == 3:
    decimalNumber = int(input("Từ DEC sang HEX!\nNhập dãy số vào: "))
    hexadecimalNumber = hex(decimalNumber)[2:].upper()
    print(f"Hệ cơ số 16 tương ứng của {decimalNumber} là {hexadecimalNumber}")

elif select == 4:
    binaryNumber = input("Từ BIN sang DEC!\nNhập dãy số vào: ")
    decimalNumber = int(binaryNumber, 2)
    print(f"Hệ cơ số 10 tương ứng của {binaryNumber} là {decimalNumber}")

elif select == 5:
    binaryNumber = input("Từ BIN sang OCT!\nNhập dãy số vào: ")
    decimalNumber = int(binaryNumber, 2)
    octalNumber = oct(decimalNumber)[2:]
    print(f"Hệ cơ số 8 tương ứng của {binaryNumber} là {octalNumber}")

elif select == 6:
    binaryNumber = input("Từ BIN sang HEX!\nNhập dãy số vào: ")
    decimalNumber = int(binaryNumber, 2)
    hexadecimalNumber = hex(decimalNumber)[2:].upper()
    print(f"Hệ cơ số 16 tương ứng của {binaryNumber} là {hexadecimalNumber}")

elif select == 7:
    octalNumber = input("Từ OCT sang DEC!\nNhập dãy số vào: ")
    decimalNumber = int(octalNumber, 8)
    print(f"Hệ cơ số 10 tương ứng của {octalNumber} là {decimalNumber}")

elif select == 8:
    octalNumber = input("Từ OCT sang BIN!\nNhập dãy số vào: ")
    decimalNumber = int(octalNumber, 8)
    binaryNumber = bin(decimalNumber)[2:]
    print(f"Số nhị phân tương ứng của {octalNumber} là {binaryNumber}")

elif select == 9:
    octalNumber = input("Từ OCT sang HEX!\nNhập dãy số vào: ")
    decimalNumber = int(octalNumber, 8)
    hexadecimalNumber = hex(decimalNumber)[2:].upper()
    print(f"Hệ cơ số 16 tương ứng của {octalNumber} là {hexadecimalNumber}")

elif select == 10:
    hexadecimalNumber = input("Từ HEX sang DEC!\nNhập dãy số vào: ")
    decimalNumber = int(hexadecimalNumber, 16)
    print(f"Hệ cơ số 10 tương ứng của {hexadecimalNumber} là {decimalNumber}")

elif select == 11:
    hexadecimalNumber = input("Từ HEX sang BIN!\nNhập dãy số vào: ")
    decimalNumber = int(hexadecimalNumber, 16)
    binaryNumber = bin(decimalNumber)[2:]
    print(f"Số nhị phân tương ứng của {hexadecimalNumber} là {binaryNumber}")

elif select == 12:
    hexadecimalNumber = input("Từ HEX sang OCT!\nNhập dãy số vào: ")
    decimalNumber = int(hexadecimalNumber, 16)
    octalNumber = oct(decimalNumber)[2:]
    print(f"Hệ cơ số 8 tương ứng của {hexadecimalNumber} là {octalNumber}")

else:
    print("Chức năng không hợp lệ. Vui lòng chọn lại.")




