import turtle

pen = turtle.Pen()
pen.left(90)
pen.pensize(10)
pen.speed(10)
pen.up()
pen.goto(-200,-200)
pen.down()
window = turtle.getscreen()

thickness = 50

def purl(side):
    pen.up()
    pen.forward(thickness)
    pen.down()
    if side:
        pen.right(90)
    else:
        pen.left(90)
    pen.forward(thickness/2)
    pen.up()
    pen.forward(4.14*thickness/10)
    pen.down()
    pen.forward(thickness/2)
    pen.up()
    pen.right(180)
    pen.forward(thickness+(2.07*thickness/10))
    if side:
        pen.right(90)
    else:
        pen.left(90)
    pen.forward(thickness/2)
    if side:
        pen.right(90)
    else:
        pen.left(90)
    pen.down()
    pen.forward(thickness)
    pen.up()
    pen.forward(2.07*thickness/10)
    if side:
        pen.right(90)
    else:
        pen.left(90)
    pen.forward(15*thickness/10)
    pen.down()

def knit(side):
    pen.forward(thickness)
    if side:
        pen.right(45)
    else:
        pen.left(45)
    pen.forward(thickness)
    if side:
        pen.right(90)
    else:
        pen.left(90)
    pen.forward(thickness)
    if side:
        pen.right(45)
    else:
        pen.left(45)
    pen.forward(thickness)

for row in range(0,6):
    for move in range(0,7):
        side = (row % 2 == 0)
        if((row % 2 == 0 and move % 2 == 0) or (row % 2 != 0 and move % 2 == 0)):
            purl(side)
            #knit(side)
        else:
            knit(side)
        pen.right(180)
    pen.up()
    pen.forward(thickness)
    pen.down()

window.exitonclick()


