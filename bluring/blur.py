"""
File: blur.py
Name:張文銓
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: a clear image with a smile face
    :return: return the same image but is more blurry
    """
    old_img = SimpleImage("images/smiley-face.png")
    new_img = SimpleImage.blank(img.width, img.height)
    for y in range(new_img.height):
        for x in range(new_img.width):
            pixel_img = old_img.get_pixel(x, y)
            pixel_new_img = new_img.get_pixel(x, y)
            sum_red = 0
            sum_blue = 0
            sum_green = 0
            count = 0
            for x_set in range(x - 1, x + 2):
                for y_set in range(y - 1, y + 2):
                    if (x_set > 0) and (y_set > 0) and (x_set < new_img.width) and (y_set < new_img.height):
                        sum_red += img.get_pixel(x_set, y_set).red
                        sum_green += img.get_pixel(x_set, y_set).green
                        sum_blue += img.get_pixel(x_set, y_set).blue
                        count += 1
            pixel_new_img.red = sum_red / count
            pixel_new_img.green = sum_green / count
            pixel_new_img.blue = sum_blue / count
    return new_img


def main():
    """
    TODO: this function turns the image to a blurry one
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
