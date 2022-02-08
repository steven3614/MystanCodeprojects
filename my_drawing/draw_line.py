"""
File: draw_line
Name: 張文銓
-------------------------
TODO: this function draw lines every two clicks while the first click will create a circle and the second click will
 make a line with the circle.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
count = 1
circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global count, circle
    # check out that whether the click is odd or even and decide what to do next
    if count % 2 == 1:
        circle = GOval(SIZE, SIZE, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        window.add(circle)
        count += 1
    elif count % 2 == 0:
        line = GLine(circle.x + SIZE / 2, circle.y + SIZE / 2, mouse.x, mouse.y)
        window.add(line)
        window.remove(circle)
        # remove the circle when we finish drawing the line
        count += 1


if __name__ == "__main__":
    main()
