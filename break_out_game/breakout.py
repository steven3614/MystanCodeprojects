"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

this function create a game that user can play with moving the paddle to hit the ball in order to
eliminate the bricks
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120  # 120 frames per second
NUM_LIVES = 3			 # Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    count = 0                                             # count is the variable that let function know when to break
    while True:
        if count < NUM_LIVES:
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())
            if graphics.ball.x <= 0:
                if graphics.get_dx() <= 0:
                    graphics.bouncing_x()
            if graphics.ball.x + graphics.ball.width >= graphics.window.width:
                if graphics.get_dx() >= 0:
                    graphics.bouncing_x()
            if graphics.ball.y <= 0:
                if graphics.get_dy() <= 0:
                    graphics.bouncing_y()
            if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                count += 1
                graphics.add_ball()
                # reset the velocity of the ball when the ball fall under the window
                graphics.vx_reset()
                graphics.vy_reset()
            if graphics.find() is False:
                graphics.bouncing_x()
                graphics.bouncing_y()
            pause(FRAME_RATE)
        if count == 3:
            break


if __name__ == '__main__':
    main()
