from turtle import *
bgcolor(0,0,0), setup(500,500)
hideturtle(), tracer(False), penup()
def rect(x = 0, y = 0, w = 100):
    goto(x, y)
    begin_fill()
    [ forward(w) or left(90) for _ in range(4) ]
    end_fill()
 
from math import sin, cos
from time import perf_counter
def _loop():
    update(), clear()
    t = perf_counter() / 2
    for i in range(200):
        a = i + t + sin(t * 2)
        Y = -25 * i ** .5
        W = (5 + 4 * sin(8 * t * cos( i ** 5))) * (1 + cos(a))
        color(1, 0.1, 0.2) if i % 2 else color(1, 1, 1)
        (i == 0) and color(1, 1, 0)
        rect(Y * sin(a) / 2, 200 + Y + Y * cos(a) / 9, int(W))
    ontimer(_loop, 10)
_loop()
mainloop()
