from turtle import *

def rectangle(l,b):
	for i in range(2):
		fd(l)
		rt(90)
		fd(b)
		rt(90)
fillcolor("green")
begin_fill()
rectangle(400,100)
end_fill()
lt(90)
fd(200)
rt(90)
fillcolor("Orange")
begin_fill()
rectangle(400,100)
end_fill()
rt(90)
fd(200)
lt(90)
fd(200)
circle(50)
lt(90)
penup()
fd(50)
pendown()
def spike():
	for i in range(24):
		color("blue")
		rt(360/24)
		fd(50)
		penup()
		rt(180)
		fd(50)
		pendown()
spike()
hideturtle()


done()