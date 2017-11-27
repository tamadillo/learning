import turtle

t = turtle.Pen()
window = turtle.getscreen()

for index in range(0,4):
    t.forward(100)
    t.right(90)

window.exitonclick()
