import turtle

# Tạo cửa sổ vẽ
screen = turtle.Screen()
screen.title("Vẽ tình cảm của tôi dành cho ") # Trên khung vẽ
screen.bgcolor("white")

# Tạo đối tượng Turtle
pen = turtle.Turtle()
pen.color('red')
pen.fillcolor('red')
pen.speed(2)

# Vẽ hình dạng trái tim
pen.begin_fill()
pen.left(140)
pen.forward(180)
pen.circle(-90, 200)
pen.left(120)
pen.circle(-90, 200)
pen.forward(180)
pen.end_fill()

# Đưa bút về vị trí giữa trên trái tim
pen.penup()
pen.goto(0, 120)  # Điều chỉnh vị trí để đặt chữ vào giữa phần rộn nhất và đẩy lên trên
pen.pendown()

# Viết chữ 'I Love You'
pen.color('white')  # Đổi màu chữ để nổi bật trên nền đỏ
pen.write("I Love Vy", align="center", font=("Arial", 18, "normal"))

# Đóng cửa sổ khi kết thúc
turtle.done()
