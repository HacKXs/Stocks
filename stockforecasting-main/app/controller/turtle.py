import turtle as t
import colorsys

t.bgcolor("black")
t.speed("fastest")
trace(100)
t.pencolor("darkvoilet")
hue = 0.7
t.hideturtle()

def func():
    global hue
    for i in range(4):
        global hue
        for i in range(4):
            color = colorsys . hsv_to_rgb(hue,1,1)
            hue+=0.001
            t.fillcolor(color)
            t.being_fill(100)
            t.fd(100)
            t.right(18)
            t.fd(100)
            t.lt(100)
            t.end_fill()
for j in range(400):
    func()
    t.goto(8, 8)
    t.rt(188)

t.exitonclick()
