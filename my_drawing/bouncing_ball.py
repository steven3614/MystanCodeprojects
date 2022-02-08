"""
File: bouncing_ball
Name: 張文銓
-------------------------
TODO: This function display a ball that fall from a position and bounce back to the air many times, however, due
 to the gravity the height of the ball bouncing back will decrease by times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked
# CONSTANT
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

# global variables
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0
# count is a variable that let the function can only run three times


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    ball.fill_color = "cyan"
    ball.color = "cyan"
    window.add(ball)
    onmouseclicked(drop)


def drop(mouse):
    global GRAVITY, REDUCE, ball, count
    if ball.x == START_X and ball.y == START_Y and count < 3:
        vy = 0
        count += 1
        # vy is the moving velocity of the y direction
        while True:
            vy += GRAVITY
            ball.move(VX, 0)
            ball.move(0, vy)
            pause(DELAY)
            if ball.y + ball.height >= window.height:
                if vy >= 0:
                    vy = (-vy) * REDUCE
            if ball.x + ball.width >= window.width:
                break
        window.add(ball, x=START_X, y=START_Y)
        # add a ball at the original position when the function breaks
        # when count = 3, the ball will not fall when we click


if __name__ == "__main__":
    main()
