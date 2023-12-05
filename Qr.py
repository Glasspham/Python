import qrcode
print('Nhập đường link dẫn bạn muốn rút gọn: ')
txt = input()
image = qrcode.make(txt)
image.save('qr.jpg')
