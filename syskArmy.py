import turtle

def drawing_shapes():
	window = turtle.Screen()
	window.bgcolor("White")

	#SYSK Army
	sysk = turtle.Turtle()
	sysk.color("Black")
	sysk.shape("arrow")
	sysk.speed(1)
	sysk.pensize(10)

	sysk.up()
	sysk.setposition(-238,300)
	sysk.down()	

	#S
	sysk.speed(4)
	sysk.left(180)
	sysk.forward(170)
	sysk.left(90)
	sysk.forward(120)
	sysk.left(90)
	sysk.forward(170)
	sysk.right(90)
	sysk.forward(120)
	sysk.right(90)
	sysk.forward(170)

	#Y
	sysk.up()
	sysk.setposition(-100,55)
	sysk.down()
	sysk.right(90)
	sysk.forward(140)
	sysk.left(45)
	sysk.forward(150)
	sysk.backward(150)
	sysk.right(90)
	sysk.forward(150)


	#S
	sysk.up()
	sysk.setposition(200,300)
	sysk.down()
	sysk.left(135)
	sysk.forward(170)
	sysk.left(90)
	sysk.forward(120)
	sysk.left(90)
	sysk.forward(170)
	sysk.right(90)
	sysk.forward(120)
	sysk.right(90)
	sysk.forward(170)

	#K
	sysk.up()
	sysk.setposition(250,55)
	sysk.down()
	sysk.right(90)
	sysk.forward(245)
	sysk.backward(140)
	sysk.right(45)
	sysk.forward(195)
	sysk.backward(175)
	sysk.right(90)
	sysk.forward(165)
	sysk.left(120)



	#Army:
	sysk.color("Red")

	#A
	sysk.up()
	sysk.setposition(-125,-120)
	sysk.down()
	sysk.forward(120)
	sysk.right(148)
	sysk.forward(120)
	sysk.right(170)
	sysk.up()
	sysk.setposition(-72,-86)
	sysk.down()
	sysk.left(63)
	sysk.forward(45)

	#r
	sysk.up()
	sysk.setposition(-25,-70)
	sysk.down()
	sysk.left(90)
	sysk.forward(50)
	sysk.left(180)
	sysk.forward(28)
	sysk.right(60)
	sysk.forward(35)

	#m
	sysk.up()
	sysk.setposition(30,-120)
	sysk.down()
	sysk.left(60)
	sysk.forward(40)
	sysk.right(90)
	sysk.forward(30)
	sysk.right(90)
	sysk.forward(40)
	sysk.backward(40)
	sysk.left(90)
	sysk.forward(30)
	sysk.right(90)
	sysk.forward(40)

	#y
	sysk.up()
	sysk.setposition(115,-50)
	sysk.down()
	sysk.left(37)
	sysk.forward(51)
	sysk.left(-75)
	sysk.backward(51)
	sysk.forward(91)
	sysk.left(35)


	sysk.hideturtle()

	window.exitonclick()
drawing_shapes()