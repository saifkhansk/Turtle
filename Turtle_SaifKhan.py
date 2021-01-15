#1

import turtle
s=turtle.Screen()
t=turtle.Turtle()

t.color('blue')
t.width(5)
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.fd(100)
t.left(120)
t.penup()
t.fd(125)

t.pendown()
t.color('green')
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.fd(100)
t.left(90)
t.penup()
t.fd(145)

t.pendown()
t.color('red')
t.fd(100)
t.left(180-(5-2)*180/5)

t.fd(100)
t.left(180-(5-2)*180/5)

t.fd(100)
t.left(180-(5-2)*180/5)

t.fd(100)
t.left(180-(5-2)*180/5)

t.fd(100)
t.left(180-(5-2)*180/5)
t.reset()

t.right(180)
t.penup()
t.fd(100)
t.right(90)
t.pendown()
t.width(5)
t.color('orange')
t.circle(200)

t.left(90)
t.penup()
t.fd(50)
t.pendown()
t.right(90)
t.color('purple')
t.circle(150)

t.left(90)
t.penup()
t.fd(50)
t.pendown()
t.right(90)
t.color('pink')
t.circle(100)

t.left(90)
t.penup()
t.fd(50)
t.pendown()
t.right(90)
t.color('yellow')
t.circle(50)



