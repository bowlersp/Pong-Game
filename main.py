from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Right_Scoreboard
from scoreboard import Left_Scoreboard
import time




screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
rightscoreboard = Right_Scoreboard()
leftscoreboard = Left_Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with top and bottom walls

    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect miss with paddle
    if ball.distance(r_paddle) > 50 and ball.xcor() > 410:
        ball.reset_position()
        leftscoreboard.increase_score_left()

    if ball.distance(l_paddle) > 50 and ball.xcor() < -410:
        ball.reset_position()
        rightscoreboard.increase_score_right()








screen.exitonclick()