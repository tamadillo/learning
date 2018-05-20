import turtle

pen = turtle.Pen()
pen.left(90)
window = turtle.getscreen()

def knit():
    pen.forward(10)
    pen.right(45)
    pen.forward(10)
    pen.right(90)
    pen.forward(10)
    pen.right(45)
    pen.forward(10)
    pen.up()
    pen.right(90)
    pen.forward(14.14213562373095)
    pen.right(90)

for start in range(0,10):
    pen.up()
    pen.forward(10)
    pen.down()
    knit()
window.exitonclick()
