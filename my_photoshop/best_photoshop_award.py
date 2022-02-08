"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage


def main():
    """
    This function is a photoshop, my idea is me watching the meteor shower because it is a beautiful phenomenon
    once I saw it and it was very impressed.
    """
    fig = SimpleImage('image_contest/steven.jpg')
    bg = SimpleImage('image_contest/star.jpg')
    bg.make_as_big_as(fig)
    new_img = combine(fig, bg)
    new_img.show()


def combine(fig, bg):
    """
    this function combine the me.image and the background into a new image.
    """
    for x in range(fig.width):
        for y in range(fig.height):
            fig_pixel = fig.get_pixel(x, y)
            avg = (fig_pixel.red + fig_pixel.green + fig_pixel.blue) // 3
            if fig_pixel.green > (1.35 * avg):
                bg_pixel = bg.get_pixel(x, y)
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
            # because the original background of me is green, so if the pixel.green is greater than a number, the
            # function will change it into the star image.
    return fig


if __name__ == '__main__':
    main()
