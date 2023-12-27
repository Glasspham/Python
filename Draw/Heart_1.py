from turtle import *
from math import sin, cos
from time import perf_counter

bgcolor(0, 0, 0)
setup(500, 500)
hideturtle()
tracer(0)
penup()

running = True  # Cờ để kiểm soát vòng lặp

def stop():
    global running
    running = False

listen()
onkeypress(stop, 'Escape')

def _loop():
    if not running:
        return  # Thoát khỏi vòng lặp khi running là False
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
    ontimer(_loop, 1)

_loop()
mainloop()
