#l.singh@jacobs-university.de
import turtle
x=-150
y=-2.5*100
t=turtle.Turtle()
t.up()
t.setpos(x,y)
t.down()
t.left(90)
t.pencolor('blue')
l=100
t.down
t.fillcolor('blue')
t.begin_fill()
t.forward(4.4*l)
t.right(123.5)
t.forward(4.135*l)
t.right(146.5)
t.forward(2.2*l)
t.left(137.5)
t.forward(3.12*l)
t.right(137.5)
t.forward(3.55*l)
t.end_fill()
t.fillcolor('red')
t.begin_fill()

b=10
t.up()
t.setpos(x+1.2*b,y+1.2*b)
t.down()
t.pencolor('red')
t.right(90)
t.forward(4.09*l)
t.right(123.5)
t.forward(3.58*l)
t.right(146.5)
t.forward(2.15*l)
t.left(137.5)
t.forward(3.12*l)
t.right(137.5)
t.forward(3.15*l)
t.end_fill()
t.up()

t.setpos(1.6*l+x,1*l+y)
t.down()
t.pencolor('white')
t.fillcolor('white')
t.begin_fill()
t.left(15)
for i in range(12):
    t.forward(30)
    t.left(120)
    t.forward(30)
    t.right(150)
t.right(15)
t.end_fill()
t.right(180)
t.up()

t.setpos(0.5*l+x,3.0*l+y)
t.down()
t.fillcolor('white')
t.begin_fill()
t.right(100)
t.circle(50,200)
t.up()
t.setpos(0.5*l+x,3.0*l+y)
t.setheading(0)
t.right(80)
t.down()
t.circle(50,160)
t.left(63)
t.end_fill()
t.up()
t.setpos(0.5*l+x,3.0*l+y)
t.setheading(280)
t.circle(50,55)

t.down()
t.left(50)
t.begin_fill()
for i in range(8):
    t.forward(10)
    t.left(120)
    t.forward(10)
    t.right(150)
t.end_fill()
