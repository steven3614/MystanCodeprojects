"""
File: sierpinski.py
Name: 張文銓
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO: this function draw triangles as many times as the ORDER wants, and the triangles get smaller and smaller
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: order is a variable that control the times that how many triangles user want to draw.
	:param length: length is variable that control how long should the sides of the triangle should be.
	:param upper_left_x: it is the x position of the upper left point of the triangle.
	:param upper_left_y: it is the y position of the upper left point of the triangle.
	:return: return the drawing on the window
	"""
	if order == 0:
		pass
	else:
		l_1 = GLine(upper_left_x, upper_left_y, upper_left_x+length, upper_left_y)
		l_2 = GLine(upper_left_x+length, upper_left_y, upper_left_x+length/2, upper_left_y+length*0.866)
		l_3 = GLine(upper_left_x+length/2, upper_left_y+length*0.866, upper_left_x, upper_left_y)
		window.add(l_1)
		window.add(l_2)
		window.add(l_3)
		pause(100)
		# upper left
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# upper right
		sierpinski_triangle(order - 1, length / 2, upper_left_x+length/2, upper_left_y)
		# bottom
		sierpinski_triangle(order - 1, length / 2, upper_left_x+length/4, upper_left_y+length*0.433)


if __name__ == '__main__':
	main()