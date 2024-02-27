from turtle import *
from math import *
from time import perf_counter
###
x = ["có", "Có", "CÓ", "được", "Được", "ĐƯỢC", "yes", "Yes", "YES", "ok", "Ok", "OK"]
y = ["không", "Không", "KHÔNG", "no", "No", "NO"]
###
def heart():
    bgcolor(0, 0, 0)
    setup(500, 500)
    hideturtle()
    tracer(0)
    penup()

    # Cờ để kiểm soát vòng lặp
    running = True  

    def stop():
        global running
        running = False

    listen()
    onkeypress(stop, 'Escape')

    def _loop():
        if not running:
            return      # Thoát khỏi vòng lặp khi running là False
        update()
        clear()
        t = perf_counter()
        X, Y = 0, 0
        for i in range(500):
            if cos(i) < 0:
                continue
            X = sin(2 - 0.2 * sin(3 * t + X / 20) ** 8 + i / 2)
            X = 200 * cos(i) * X
            Y = 200 * sin(i + 0.7 ** cos(i) ** 0.05) - 30
            goto(X, Y)
            dot(20, (1, 0, sin(i + t + sin(t / 2)) / 2 + .5))      
        # Ghi tên vào giữa trái tim
        penup()
        goto(0, -50) # Điều chỉnh vị trí để ghi tên ở giữa trái tim
        color("white") # Đổi màu chữ 
        write("name1", align="center", font=("Arial", 40, "normal")) # Đổi tên và kích thước chữ 
        ontimer(_loop, 1)
    _loop()
    mainloop()
###
def thich(a):
    if a in x:
        b = input('Nhưng tôi còn yêu em nữa <3\nVậy em có yêu tôi không? ')
        return b
    
    elif a in y:
        print('Em nên suy nghĩ lại đi')
        return input('Tôi thích em\nEm có thích tôi không? ')
    
    else:
        print('Xin lỗi, tôi không hiểu. Vui lòng trả lời lại')
        return input('Tôi thích em\nEm có thích tôi không? ')
###
def yeu(b):
    if b in x:
        c = input('Vậy em đồng ý làm bạn gái tôi nhé? ')
        return c
    
    elif b in y:
        print('Em nên suy nghĩ lại đi')
        return input('Nhưng tôi còn yêu em nữa <3\nVậy em có yêu tôi không? ')
    
    else:
        print('Xin lỗi, tôi không hiểu. Vui lòng trả lời lại')
        return input('Nhưng tôi còn yêu em nữa <3\nVậy em có yêu tôi không? ')
###        
def thanhcong(c):
    if c in x:
        print('Vậy chúng ta đã chính thức là người yêu của nhau <3')
        heart()

    elif c in y:
        print('Em nên suy nghĩ lại đi')
        return input('vậy em đồng ý làm bạn gái tôi nhé? ')
    
    else:
        print('Xin lỗi, tôi không hiểu. Vui lòng trả lời lại')
        return input('vậy em đồng ý làm bạn gái tôi nhé? ')        
###    
if __name__ == "__main__":
    print('Xin chào name1 dễ thương nha <3') # Đổi name1 thành tên người bạn muốn gửi đến là được
    print('Và sau đây sẽ là một số câu hỏi mình dành cho bạn.')
    print('Những câu hỏi có thể trả "yes, no" hoặc "có, không".')
    z = input('Hãy nhấn Enter để tiếp tục.')

    # Câu hỏi đầu tiên        
    a = input('Tôi thích em\nEm có thích tôi không? ')
    
    # Câu hỏi thứ 2
    b = thich(a)
    if b is not None:
        c = yeu(b)
    
    # Câu hỏi thứ 3    
    if c is not None:
        thanhcong(c)  
