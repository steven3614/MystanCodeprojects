"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

this is the function that create class and methods in order to make the main function more easier to see and work

"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40  # Height of a brick (in pixels)
BRICK_HEIGHT = 15  # Height of a brick (in pixels)
BRICK_ROWS = 10  # Number of rows of bricks
BRICK_COLS = 10  # Number of columns of bricks
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10  # Radius of the ball (in pixels)
PADDLE_WIDTH = 75  # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels)
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball
MAX_X_SPEED = 5  # Maximum initial horizontal speed for the ball

count = 0


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.paddle.color = 'black'
        self.paddle.fill_color = 'black'
        self.window.add(self.paddle, x=(self.window.width / 2) - self.paddle.width / 2, y=(self.window.height -
                                                                                           PADDLE_OFFSET))
        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.ball.fill_color = 'red'
        self.ball.color = 'red'
        self.window.add(self.ball, x=(self.window.width / 2) - self.ball.width / 2,
                        y=(self.window.height / 2) - self.ball
                        .height / 2)
        # Default initial velocity for the ball
        self.__dy = 0
        self.__dx = 0
        # Draw bricks
        color_list = ['light grey', 'grey', 'dark grey', 'dim grey', 'black']
        color_counter = -1
        for i in range(BRICK_COLS):
            if i % 2 == 0:
                color_counter += 1
            for j in range(BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                color = color_list[color_counter % len(color_list)]
                self.brick.fill_color = color
                self.brick.color = color
                self.window.add(self.brick, x=(BRICK_WIDTH + BRICK_SPACING) * j, y=BRICK_OFFSET + (BRICK_HEIGHT +
                                                                                                   BRICK_SPACING) * i)
        # Initialize our mouse listeners
        onmousemoved(self.move)
        onmouseclicked(self.start)

    def move(self, mouse):
        if self.window.width > mouse.x + PADDLE_WIDTH / 2 and mouse.x - PADDLE_WIDTH / 2 > 0:
            self.paddle.x = mouse.x - PADDLE_WIDTH / 2
            self.paddle.y = self.window.height - PADDLE_OFFSET

    def start(self, mouse=0):
        if self.ball.x == (self.window.width / 2) - self.ball.width / 2 and self.ball.y == (self.window.height / 2) - (
                self.ball.height / 2):
            self.__dy = INITIAL_Y_SPEED
            self.__dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self.__dx = -self.__dx

    def find(self):
        pos_1 = self.window.get_object_at(self.ball.x, self.ball.y)
        pos_2 = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y)
        pos_3 = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2)
        pos_4 = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2)
        if pos_1 is not None:
            if pos_1 == self.paddle:
                if self.__dy <= 0:
                    return False
            else:
                self.window.remove(pos_1)
                return False
        elif pos_2 is not None:
            if pos_2 == self.paddle:
                if self.__dy <= 0:
                    return False
            else:
                self.window.remove(pos_2)
                return False
        elif pos_3 is not None:
            if pos_3 == self.paddle:
                if self.__dy >= 0:
                    return False
            else:
                self.window.remove(pos_3)
                return False
        elif pos_4 is not None:
            if pos_4 == self.paddle:
                if self.__dy >= 0:
                    return False
            else:
                self.window.remove(pos_4)
                return False

    def add_ball(self):
        # add a ball when the ball is out of the window
        self.window.add(self.ball, x=(self.window.width / 2) - self.ball.width / 2,
                        y=(self.window.height / 2) - self.ball.height / 2)

    def get_dy(self):
        return self.__dy

    def get_dx(self):
        return self.__dx

    def bouncing_x(self):
        # now self.__dx = -self.__dx because it will only bounce to the opposite direction, the player can know where
        # the ball go easily
        self.__dx = -random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def bouncing_y(self):
        self.__dy = -self.__dy

    def vx_reset(self):
        self.__dx = 0

    def vy_reset(self):
        self.__dy = 0
