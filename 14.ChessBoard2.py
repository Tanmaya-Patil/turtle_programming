import turtle

t = turtle.Turtle()
t.speed = 0.5
t.color("black")

def square(n):
    for i in range(n):
        t.forward(320)
        t.left(90)
square(4)

t.color("black","black")
def sq1(n):
    t.begin_fill()
    for i in range(n):
        t.forward(40)
        t.left(90)
        t.forward(40)
        t.left(90)
        t.forward(40)
        t.right(90)
        t.forward(40)
        t.right(90)
    t.end_fill()
sq1(4)

t.forward(40)
    
def sq2(n):
    t.begin_fill()
    for i in range(n):
        t.forward(40)
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(40)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()
sq2(4)
t.forward(40)

sq1(4)
t.forward(40)
sq2(4)
t.forward(40)

sq1(4)
t.forward(40)
sq2(4)
t.forward(40)

sq1(4)
t.forward(40)
sq2(4)
t.forward(40)



