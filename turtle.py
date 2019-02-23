import turtle
wn = turtle.Screen()
juan = turtle.Turtle()
numofsides=int(input("What is the n of the sides ?"))
lengofsides=int(input("what is the length of the side ?"))
colorline=str(input("what is the color ?"))
fcolor=str(input("What is the fill color of the regular polygon ?"))
angle = 360 / numofsides

juan.begin_fill()
juan.fillcolor(fcolor)
juan.color(colorline)
for i in range(numofsides):
    juan.forward(lengofsides)
    juan.left(angle)

juan.end_fill()
