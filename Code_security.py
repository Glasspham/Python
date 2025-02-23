#? Bảo vệ code bằng password
import getpass
password = getpass.getpass("Enter your password: ")
if password != 'secret':
    print('Access Denied')
    exit()
else:
    print('Access Granted')
    #TODO Your protected code here
