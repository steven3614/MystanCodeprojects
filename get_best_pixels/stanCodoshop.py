"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO: This function shows a picture that is the best picture among the given pictures, the best picture means that
    it consists of best pixels, which has the shortest color distance.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (float): color distance between red, green, and blue pixel values

    """
    # color_dis calculate the distance between the pixel and the average
    color_dis = ((red-pixel.red) ** 2 + (green-pixel.green) ** 2 + (blue-pixel.blue) ** 2) ** (1/2)
    return color_dis


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    l_pixels = len(pixels)
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    for i in range(l_pixels):
        # ele is the variable that storage the elements of pixels list
        ele = pixels[i]
        sum_red += ele.red
        sum_green += ele.green
        sum_blue += ele.blue
    avg_red = sum_red // l_pixels
    avg_green = sum_green // l_pixels
    avg_blue = sum_blue // l_pixels
    avg = [avg_red, avg_green, avg_blue]
    return avg


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    pixels.append(get_average(pixels))
    l_pixels = len(pixels)
    short_dis = 20000
    short_pixel = []
    avg = get_average(pixels)
    for i in range(l_pixels-1):
        dis = get_pixel_dist(pixels[i], avg[0], avg[1], avg[2])
        if dis < short_dis:
            short_dis = dis
            short_pixel = pixels[i]
    return short_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(result.width):
        for y in range(result.height):
            pixels = []
            for image in images:
                pixels.append(image.get_pixel(x, y))
            best = get_best_pixel(pixels)
            result.set_pixel(x, y, best)
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
