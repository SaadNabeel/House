import turtle
turtle.Screen().bgcolor("Orange")
t=turtle.Turtle()
t.shape("turtle")
t.color("red")
t.penup()
t.goto(-200,180)
t.pendown()
for c in range(2):
    t.forward(500)
    t.right(90)
    t.forward(50)
    t.right(90)
t.penup()
t.goto(-170,130)
t.pendown()
for c in range(2):
    t.forward(420)
    t.right(90)
    t.forward(420)
    t.right(90)

turtle.done()