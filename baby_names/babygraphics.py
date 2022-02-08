"""
File: babygraphics.py
Name: steven
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    pos_x = int((width/len(YEARS))*int(year_index))
    return pos_x


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the rank of the current year
    returns the y coordinate where the rank should be drawn.

    Input:
        height (int): The height of the canvas
        rank (str): The rank number
    Returns:
        y_coordinate (int): The y coordinate of the rank.
    """
    pass


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #

    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, width=LINE_WIDTH)

    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, width=
    LINE_WIDTH)

    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2*GRAPH_MARGIN_SIZE, i),
                           0, GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE,
                            i), CANVAS_HEIGHT, width=LINE_WIDTH)
        canvas.create_text(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH-2*GRAPH_MARGIN_SIZE, i) + TEXT_DX,
                           CANVAS_HEIGHT, text=YEARS[i], anchor=tkinter.SW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """

    draw_fixed_lines(canvas)        # draw the fixed background grid
    # ----- Write your code below this line ----- #
    x_pos = int((CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE)/len(YEARS))
    y_pos = (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE)/MAX_RANK

    for i in range(len(lookup_names)):
        name = lookup_names[i]
        for j in range(len(YEARS)-1):
            if str(YEARS[j]) in name_data[name]:
                num = int(name_data[name][str(YEARS[j])])

            else:
                num = 10000

            if str(YEARS[j+1]) in name_data[name]:
                num_1 = int(name_data[name][str(YEARS[j+1])])

            else:
                num_1 = 10000

            if num > 1000 and num_1 > 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_pos, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   GRAPH_MARGIN_SIZE + (j+1)*x_pos,
                                   CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_pos, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   text=name+' *', fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)

            elif num > 1000 > num_1:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_pos, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_pos, GRAPH_MARGIN_SIZE + (num_1 * y_pos),
                                   fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_pos, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   text=name + ' *', fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)

            elif num < 1000 < num_1:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_pos, GRAPH_MARGIN_SIZE + num * y_pos,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_pos, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                                   fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                ans = ""
                ans = str(name) + str(num)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_pos, GRAPH_MARGIN_SIZE + num * y_pos,
                                   text=ans, fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)

            elif num < 1000 and num_1 < 1000:
                canvas.create_line(GRAPH_MARGIN_SIZE + j * x_pos, GRAPH_MARGIN_SIZE + num * y_pos,
                                   GRAPH_MARGIN_SIZE + (j + 1) * x_pos, GRAPH_MARGIN_SIZE + num_1 * y_pos,
                                   fill=COLORS[i % len(COLORS)], width=LINE_WIDTH)
                ans = ""
                ans = str(name) + str(num)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + j * x_pos, GRAPH_MARGIN_SIZE + num * y_pos,
                                   text=ans, fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)
            if j == 10:
                ans = ""
                ans = str(name) + str(num)
                canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + 11 * x_pos, GRAPH_MARGIN_SIZE + num * y_pos,
                                   text=ans, fill=COLORS[i % len(COLORS)], anchor=tkinter.SW)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
