import turtle
import math

def draw_spirograph(R,r,p_c):
    turtle.up()
    x = (R-r)*math.cos(0) + p_c*math.cos(((R-r)/r)*0)
    y = (R-r)*math.sin(0) + p_c*math.sin(((R-r)/r)*0)
    turtle.setpos(x,y)
    turtle.down()
    for i in range(0,360*r,5):
        a = math.radians(i)
        x = (R-r)*math.cos(a) + p_c*math.cos(((R-r)/r)*a)
        y = (R-r)*math.sin(a) - p_c*math.sin(((R-r)/r)*a)
        turtle.setpos(x,y)

draw_spirograph(220,72,50)

turtle.mainloop()