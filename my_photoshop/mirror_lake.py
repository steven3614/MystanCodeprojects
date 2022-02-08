"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: the image of the lake
    :return: return the mirror lake with the original one together.
    """

    img = SimpleImage("images/mt-rainier.jpg")
    new_img = SimpleImage.blank(img.width, img.height * 2)
    for x in range(img.width):
        for y in range(img.height):
            old_p = img.get_pixel(x, y)
            # flip the new img to the down of the original picture.
            new_p_up = new_img.get_pixel(x, y)
            new_p_up.red = old_p.red
            new_p_up.green = old_p.green
            new_p_up.blue = old_p.blue
            new_p_down = new_img.get_pixel(x, new_img.height - 1 - y)
            new_p_down.red = old_p.red
            new_p_down.green = old_p.green
            new_p_down.blue = old_p.blue
    new_img.show()


def main():
    """
    This function flip the image downward and looks like a mirror.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflect("images/mt-rainier.jpg")


if __name__ == '__main__':
    main()
