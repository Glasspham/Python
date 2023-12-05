import pyshorteners
print('Nhập đường link dẫn bạn muốn rút gọn: ')
txt = input()
long_url= txt
shortener = pyshorteners.Shortener()
short_url = shortener.tinyurl.short(long_url)
print("Đây là đường link đã rút gọn: ",short_url)