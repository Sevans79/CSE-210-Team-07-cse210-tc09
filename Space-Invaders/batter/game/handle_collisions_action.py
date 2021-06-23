import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self):
        
        self.score = 0


    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # there's only one
        paddle = cast["paddle"][0] # there's only one
        bricks = cast["brick"]

        # gets current position and velocity values from ball
        x_Position = ball.get_position()
        x_Position = x_Position.get_x()
        y_Position = ball.get_position()
        y_Position = y_Position.get_y()
        y_Velocity = ball.get_velocity()
        y_Velocity = y_Velocity.get_y()
        x_Velocity = ball.get_velocity()
        x_Velocity = x_Velocity.get_x()

        #recognizes when ball hits bottom of the screen and bounces the ball
        #this is where the game needs to end
        if y_Position == 19:
            # velocity = Point(x_Velocity, -1)
            # ball.set_velocity(velocity)
            score = self.score
            score = str(score)
            ball.set_text("Game Over, Your score is: " + score)
            ball.set_position(Point(30,10))
            ball.set_velocity(Point(0,0))


        #bounces off ceiling
        if y_Position == 1:
            velocity = Point(x_Velocity, 1)
            ball.set_velocity(velocity)


        #checks if ball is coliding with a brick, changes y_velocity if it is
        for i in range(280):
            brick = bricks[i]
            if brick.get_position().equals(ball.get_position()):
                self.score += 1
                velocity = Point(x_Velocity, y_Velocity * -1)
                ball.set_velocity(velocity)
                brick.set_text('')
                brick.set_position(Point(1,1))
                
        
        # checks if ball is coliding with paddle, changes y_velocity if it is
        for i in range(6):
            pos = ball.get_position().add(Point(-i,0))
            if paddle.get_position().equals(pos):
                velocity = Point(-1, -1)
                ball.set_velocity(velocity)
        
        for i in range(5):
            i += 6
            pos = ball.get_position().add(Point(-i,0))
            if paddle.get_position().equals(pos):
                velocity = Point(1, -1)
                ball.set_velocity(velocity)

        # checks if ball is coliding with left and right borders, changes x_velocity if it is
        if x_Position >= 79:
            velocity = Point(-1, y_Velocity)
            ball.set_velocity(velocity)
        if x_Position <= 1:
            velocity = Point(1, y_Velocity)
            ball.set_velocity(velocity)

