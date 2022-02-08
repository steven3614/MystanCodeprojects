"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, file name of the image that need to be shrink.
    :return img: SimpleImage, an image that is 1/2 size of the original one.
    """
    img = SimpleImage("images/poppy.png")
    new_img = SimpleImage.blank(img.width // 2, img.height // 2)
    # let the new image be the 1/2 size of the original one
    for x in range(img.width):
        for y in range(img.height):
            old_p = img.get_pixel(x, y)
            new_p = new_img.get_pixel(x // 2, y // 2)
            new_p.red = old_p.red
            new_p.green = old_p.green
            new_p.blue = old_p.blue
    new_img.show()


def main():
    """
    show the original image and the image that is shrink by 1/2.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    shrink("images/poppy.png")

if __name__ == '__main__':
    main()
