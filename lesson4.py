import turtle as t
import random as r 
t.bgcolor ("#b4cddb")
t.speed(0)

#sand-bottom :)
t.penup()
t.goto(-500,-150)
t.pendown()
t.color("#aba98e","#c9c7a1")
t.width (2)
t.begin_fill ()
for x in range (2):
    t.forward (1000)
    t.right (90)
    t.forward (200)
    t.right (90)
t.end_fill()

#sand-dots
for i in range (30):
    x = r.randint (-500,500)
    y = r.randint (-350,-150)
    t.penup ()
    t.goto(x,y)
    t.pendown ()
    t.circle(1)

t.penup ()
t.goto (-300,-150)
t.pendown ()

t.color ("#a88f32","#e8d07b")
t.begin_fill ()

for x in range (3):
    t.forward (300)
    t.left(120)

t.end_fill ()

t.penup ()
t.goto (250,-150)
t.pendown ()

t.color ("#023800","#056e01")
t.begin_fill ()

t.setheading (90)

t.forward (70)

t.setheading (0)

t.circle(40,180)

t.setheading(90)

t.forward (120)

t.circle (40,180)

t.setheading (270)

t.forward (40)

t.setheading (180)

t.circle(40,180)

t.setheading (270)

t.forward (150)

t.end_fill ()

t.mainloop ()
