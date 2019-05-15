import turtle 
turtle.speed(30)

turtle.goto(0,0)
colors = ["Red","blue","yellow","green"]
for i in range(300):
    turtle.pencolor(colors[i%4])
    turtle.circle(i)
    turtle.left(91)
input("press Enter:")    
