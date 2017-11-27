import turtle

t = turtle.Pen()
window = turtle.getscreen()

def square():
    for index in range(0,4):
        t.forward(100)
        t.right(90)

for start in range(0,10):
    square()
    t.left(90)
    t.up()
    t.forward(10)
    t.right(90)
    t.forward(10)
    t.down()

window.exitonclick()
