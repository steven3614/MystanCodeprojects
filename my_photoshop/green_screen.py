"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: background is the picture we want to be with the character
    :param figure_img: figure_img is the green picture with the character
    :return:
    """
    img = SimpleImage("images/ReyGreenScreen.png")
    space_img = SimpleImage("images/MillenniumFalcon.png")
    for y in range(img.height):
        for x in range(img.width):
            pixel_img = img.get_pixel(x, y)
            if pixel_img.green > (pixel_img.blue * 2) and pixel_img.green > (pixel_img.red * 2):
                pixel_space = space_img.get_pixel(x, y)
                pixel_img.red = pixel_space.red
                pixel_img.blue = pixel_space.blue
                pixel_img.green = pixel_space.green
                # change the pixel when the green pixel is greater than twice of the bigger one among red and blue.
    return img


def main():
    """
    we show the combined picture of the figure and the background.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()
    figure.show()
    space_ship.show()


if __name__ == '__main__':
    main()
