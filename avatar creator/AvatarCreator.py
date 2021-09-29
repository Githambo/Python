import turtle
import random

t = turtle.Turtle()
t.speed(30)
def drawFace():
	#Drawing the face
	t.penup()
	t.goto(0,-150)
	t.color('black')
	t.fillcolor('brown')
	t.begin_fill()
	t.circle(150)
	t.end_fill()

def drawEyes():
	#Draw the Left eye
    t.goto(-95, 45)
    t.down()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.up()
    # Draw the left eye pupils
    t.goto(-95, 39)
    t.down()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(12)
    t.end_fill()
    t.up()

    #Draw the right eye
    t.goto(95, 40)
    t.down()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.up()

 	# Draw the left eye pupil
    t.goto(95, 39)
    t.down()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(12)
    t.end_fill()
    t.up()
def DrawNose():
	t.goto(0,0)
	t.fillcolor('black')
	t.begin_fill()
	t.circle(10)
	t.end_fill()
	t.up()

def DrawMouth():
	t.pensize(10)
	t.goto(-40, -50)
	t.down()
	t.right(90)
	t.circle(50, 180)
	t.up()

def drawHair():
  #Drawing the hair
  t.penup()
  t.goto(0,100)
  t.pendown()
  t.color('black')
  t.fillcolor('black')
  t.begin_fill()
  t.goto(-160,20+random.randint(-10,10))
  t.goto(-140,110+random.randint(-10,10))
  t.goto(-130,100+random.randint(-10,10))
  t.goto(-110,160+random.randint(-10,10))
  t.goto(-90,150+random.randint(-10,10))
  t.goto(-70,180+random.randint(-10,10))
  t.goto(-50,160+random.randint(-10,10))
  t.goto(-40,190+random.randint(-10,10))
  t.goto(-10,160+random.randint(-10,10))
  t.goto(20,180+random.randint(-10,10))
  t.goto(50,160+random.randint(-10,10))
  t.goto(70,150+random.randint(-10,10))
  t.goto(90,160+random.randint(-10,10))
  t.goto(110,140+random.randint(-10,10))
  t.goto(130,170+random.randint(-10,10))
  t.goto(140,110+random.randint(-10,10))
  t.goto(160,20+random.randint(-10,10))
  t.goto(-50,-50)
  t.end_fill()
   
    
    
    
   


drawHair()
drawFace()
drawEyes()
DrawNose()
DrawMouth()

t.screen.exitonclick()