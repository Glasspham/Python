from turtle import *
bgcolor(0,0,0), setup(500,500)
hideturtle(), tracer(0), penup()

from math import sin, cos
from time import perf_counter
def _Oneo_Kuu():
    update(), clear()
    t = perf_counter()
    for i in range(400):
        if cos(i) < 0: continue
        X = sin(2 - 0.4 * sin(4 * t + sin(4 * t)) ** 4 + i / 2)
        X = (200 + 10 * cos(t - sin(4 * t))) * cos(i) * X
        Y = sin(i + 0.7 ** cos(i) ** 0.05)
        Y = (200 + 10 * sin(t - sin(4 * t))) * Y - 30
        color = (sin(i + t + sin(t / 2) ) / 3 + 1 / 3, 1, 0)
        goto(X, Y)
        dot (30 + 3 * sin(X / 20 + t * 5), color)
    ontimer(_Oneo_Kuu, 10)
_Oneo_Kuu( )
mainloop( )
