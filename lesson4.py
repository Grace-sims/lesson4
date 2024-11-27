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
    t.forward (700)
    t.right (90)
    t.forward (200)
    t.right (90)
t.end_fill()

#sand-dots
for i in range (30):
    x = r.randint (-500,200)
    y = r.randint (-350,-150)
    t.penup ()
    t.goto(x,y)
    t.pendown ()
    t.circle(1)

t.mainloop ()