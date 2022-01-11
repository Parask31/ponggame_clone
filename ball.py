from turtle import  Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Brings the ball back to (0, 0) position and resets the speed that is increase sleep time --> time.sleep(____)
    def reset_ball(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.1

    # Gives the ball its movement
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Changes y_move number's sign
    def bounce_y(self):
        self.y_move *= -1

    # Changes x_move number's sign and the move speed is to reduce sleep time of loop and increase speed of ball each
    # time it hits any paddle
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9
