"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: images/ greenland-fire.png
    :return: the image of the fire
    """
    img = SimpleImage("images/greenland-fire.png")
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) / 3
        if pixel.red > avg:
            # when the red pixel is greater than average, that is the position we are going to show that is red.
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            # other position turn into gray.
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    img.show()


def main():
    """
    This function shows the position of the fire, let the user clearly notice the situation.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlight_fires("images/greenland-fire.png")


if __name__ == '__main__':
    main()
