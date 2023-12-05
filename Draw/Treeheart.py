import turtle

t = turtle.Turtle()
t.screen.bgcolor("black")
t.pensize(3)
t.color("brown")
t.left(90)
t.backward(80)
t.speed(0)

# Tạo hình trái tim với kích thước nhỏ hơn
def draw_heart(x, y, size):
    heart = turtle.Turtle()
    heart.color('red')
    heart.speed(0)

    # Di chuyển đến vị trí trên cây
    heart.penup()
    heart.goto(x, y)
    heart.pendown()

    # Vẽ hình trái tim với kích thước nhỏ hơn
    heart.left(140)
    heart.begin_fill()
    heart.circle(-size, 200)
    heart.left(120)
    heart.circle(-size, 200)
    heart.end_fill()
    heart.hideturtle()

def tree(i):
    if i < 15:
        return
    else:
        t.forward(i)
        t.color("red")
        t.circle(4)
        t.color("aqua")
        x, y = t.position()  # Lưu vị trí hiện tại của turtle
        t.left(30)
        tree(3 * i / 4)
        draw_heart(x, y, 8)  # Vẽ hình trái tim nhỏ với bán kính 15
        t.right(60)
        tree(3 * i / 4)
        t.left(30)
        t.backward(i)

tree(90)
turtle.done()
