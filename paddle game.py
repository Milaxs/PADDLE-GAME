import turtle
import winsound
WIDTH = 1000
HEIGHT = 500
#create a display
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)
screen.bgcolor("black")
#creating score variable
score_a = 0
score_b = 0

#Creating the 1st paddle
paddle_a = turtle.Turtle()
paddle_a.penup()
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.bk(450)
paddle_a.shape('square')
paddle_a.shapesize(8,1)

#Creating the 2nd paddle
paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.speed(0)
paddle_b.speed(0)
paddle_b.color('white')
paddle_b.fd(450)
paddle_b.shape('square')
paddle_b.shapesize(8,1)

#Creating the 1st Ball
ball1 = turtle.Turtle()
ball1.penup()
ball1.speed(0)
ball1.shape('circle')
ball1.color('white')
ball1.dx = 10
ball1.dy = 10

#Creating our Text
pen = turtle.Turtle()
pen.penup()
pen.speed(0)
pen.color("white")
pen.goto(0,200)
pen.hideturtle()
pen.write("Player A: 0 Player B: 0", align = "center", font = ("arial", 24, "bold") )

#Creating our 2nd ball
ball2 = turtle.Turtle()
ball2.penup()
ball2.speed(0)
ball2.shape("circle")
ball2.color("white")
ball2.dx = -10
ball2.dy = -10

#determines the speed in which the paddle moves
def paddle_up():
    y = paddle_a.ycor()
    y += 15
    paddle_a.sety(y)

def paddle_down():
    y = paddle_a.ycor()
    y -= 15
    paddle_a.sety(y)

def paddle_up1():
    y = paddle_b.ycor()
    y += 15
    paddle_b.sety(y)

def paddle_down1():
    y = paddle_b.ycor()
    y -= 15
    paddle_b.sety(y)

#screen.listen() allow the user to access keys on the keyboard 
screen.listen()
#we assign the keys here
screen.onkeypress(paddle_up, 'w')
screen.onkeypress(paddle_down, 's')
screen.onkeypress(paddle_up1, 'Up')
screen.onkeypress(paddle_down1, 'Down')

while True:
    screen.update()
    #Allows the ball to move
    ball1.setx(ball1.xcor() + ball1.dx)
    ball1.sety(ball1.ycor() + ball1.dy)

    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)
    #setting boundary for the ball
    if ball1.ycor() > 230:
        ball1.sety(230)
        ball1.dy*= -1
        winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)


    if ball1.ycor() < -230:
        ball1.sety(-230)
        ball1.dy*= -1
        winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)


    if ball1.xcor() < -470:
        ball1.goto(0,0)
        winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)

        #score code 
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font = ("arial", 24, "bold") )
    if score_b == 5:
        pen.clear()
        pen.write(f"Player B is the winner", align="center", font = ("arial", 24, "bold"))
        break
                
    if ball1.xcor() > 470:
       ball1.goto(0,0)
       winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)

       score_a += 1
       pen.clear()
       pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font = ("arial", 24, "bold") )
    if score_a == 5:
        pen.clear()
        pen.write(f"Player A is the winner", align="center", font = ("arial", 24, "bold"))
        break

       
    if ball2.ycor() > 230:
        ball2.sety(230)
        ball2.dy*= -1
        winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)

    if ball2.ycor() < -230:
        ball2.sety(-230)
        ball2.dy*= -1
        winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)

    if ball2.xcor() < -470:
        ball2.goto(0,0)
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font = ("arial", 24, "bold") )
        winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)

        
    if ball2.xcor() > 470:
       ball2.goto(0,0)
       score_a += 1
       pen.clear()
       pen.write(f"Player A: {score_a} Player B: {score_b}", align = "center", font = ("arial", 24, "bold") )
       winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)

        
    #setting boundary for paddle
    if paddle_a.ycor() > 200:
        paddle_a.goto(-450, 180)

    if paddle_a.ycor() < -200:
        paddle_a.goto(-450, -180)

    if paddle_b.ycor() >200:
        paddle_b.goto(450, 180)

    if paddle_b.ycor() < -200:
        paddle_b.goto(450, -180)

    #ball bouncing on paddle
    if ball1.xcor() > 430 and ball1.xcor() < 450 and (ball1.ycor() < paddle_b.ycor() + 80 and ball1.ycor() > paddle_b.ycor() - 80):
       ball1.setx(430)
       ball1.dx *= -1
       winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)
       
    if ball1.xcor() < -430 and ball1.xcor() > -450 and (ball1.ycor() < paddle_a.ycor() + 80 and paddle_a.ycor() > paddle_a.ycor() - 80):
       ball1.setx(-430)
       ball1.dx *= -1
       winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)
       
    if ball2.xcor() > 430 and ball2.xcor() < 450 and (ball2.ycor() < paddle_b.ycor() + 80 and paddle_b.ycor() > paddle_b.ycor() - 80):
       ball2.setx(430)
       ball2.dx *= -1
       winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)
       
    if ball2.xcor() < -430 and ball2.xcor() > -450 and (ball2.ycor() < paddle_a.ycor() + 80 and ball2.ycor() > paddle_a.ycor() - 80):
       ball2.setx(-430)
       ball2.dx *= -1
       winsound.PlaySound("C:/Users/OSAG 16/Desktop/HTML/python/SPRTField_Balloon against wall 2 (ID 1826)_BSB", winsound.SND_ASYNC)
       
       
