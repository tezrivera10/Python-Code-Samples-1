#Raul Rivera
#2/28/19

#Drawing an square over squares using turtle

import turtle

def drawSquare(b,ft):
     for i in range (4):
        b.forward(ft)
        b.left(90)
        
        

wn = turtle.Screen()


bobby = turtle.Turtle()
bobby.color ("green")
size = [20,40,60,80,100]
for x in size:
    drawSquare ( bobby,x)
    bobby.penup()
    bobby.backward(10)
    bobby.right (90)
    bobby.forward (10)
    bobby.left(90)
    bobby.pendown()

#DrawSquare (bobby,9)

wn.exitonclick()
