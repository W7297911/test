# coding=utf-8
# Version:python3.6.0
# Tools:Pycharm 2017.3.2
# Date:2018-12-02 22:17
# Author:Wangyafei

from turtle import Turtle as t

t.speed('fast')
t.hideturtle()
t.bgcolor('black')
i = 0
while i < 135:
    t.pencolor('red')
    t.penup()
    t.goto(0, 0)
    t.fd(200)
    t.pendown()
    t.circle(100)
    t.left(2)
    i += 1
