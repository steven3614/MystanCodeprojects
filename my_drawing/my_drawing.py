"""
File: my_drawing
Name: 張文銓
----------------------
TODO: This function is my drawing about the famous show "squid game" including the killer and the invitation card
 in the story.
"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: I drew different items and named them by numbers because there are too many items.
    the whole picture is about the famous show squid game.
    """
    window = GWindow(width=800, height=790, title='Squid Game')
    # this is the window of the picture
    one = GOval(230, 300, x=30, y=130)
    one.filled = True
    one.fill_color = 'palevioletred'
    one.color = 'palevioletred'
    window.add(one)

    two = GOval(230, 300, x=280, y=100)
    two.filled = True
    two.fill_color = 'palevioletred'
    two.color = 'palevioletred'
    window.add(two)

    three = GOval(230, 300, x=530, y=130)
    three.filled = True
    three.fill_color = 'palevioletred'
    three.color = 'palevioletred'
    window.add(three)

    four = GOval(210, 280, x=40, y=140)
    four.filled = True
    four.fill_color = 'black'
    four.color = 'black'
    window.add(four)

    five = GOval(210, 280, x=290, y=110)
    five.filled = True
    five.fill_color = 'black'
    five.color = 'black'
    window.add(five)

    six = GOval(210, 280, x=540, y=140)
    six.filled = True
    six.fill_color = 'black'
    six.color = 'black'
    window.add(six)
    # one to six are the items for the mask of the killer
    seven = GOval(150, 150, x=72.5, y=205)
    seven.color = 'white'
    seven.filled = True
    seven.fill_color = 'white'
    window.add(seven)

    eight = GOval(125, 125, x=85, y=217.5)
    eight.filled = True
    eight.fill_color = 'black'
    eight.color = 'black'
    window.add(eight)

    nine = GRect(150, 150, x=320, y=185)
    nine.filled = True
    nine.fill_color = 'white'
    nine.color = 'white'
    window.add(nine)

    ten = GRect(125, 125, x=332.5, y=197.5)
    ten.filled = True
    ten.fill_color = 'black'
    ten.color = 'black'
    window.add(ten)

    eleven = GLabel('^', x=585, y=490)
    eleven.color = 'white'
    eleven.font = '-300'
    window.add(eleven)

    twelve = GLabel('-', x=580, y=460)
    twelve.color = 'white'
    twelve.font = '-300'
    window.add(twelve)
    # seven to twelve are the items on the mask(square, circle and triangle)
    thirteen = GRect(400, 250, x=200, y=490)
    thirteen.filled = True
    thirteen.fill_color = 'khaki'
    window.add(thirteen)
    # this is the item for the invitation card
    fourteen = GLabel('WELCOME TO THE SQUID GAME!', x=210, y=525)
    fourteen.color = 'red'
    fourteen.font = '-25'
    window.add(fourteen)

    fifteen = GOval(90, 90, x=225, y=570)
    fifteen.filled = True
    fifteen.fill_color = 'black'
    fifteen.color = 'black'
    window.add(fifteen)

    sixteen = GRect(90, 90, x=350, y=570)
    sixteen.filled = True
    sixteen.fill_color = 'black'
    sixteen.color = 'black'
    window.add(sixteen)

    seventeen = GLabel('^', x=465, y=840)
    seventeen.font = "-300"
    seventeen.color = "black"
    window.add(seventeen)

    eighteen = GLabel('-', x=460, y=805)
    eighteen.font = "-300"
    eighteen.color = "black"
    window.add(eighteen)

    nineteen = GOval(70, 70, x=235, y=580)
    nineteen.filled = True
    nineteen.fill_color = 'khaki'
    nineteen.color = 'khaki'
    window.add(nineteen)

    twenty = GRect(70, 70, x=360, y=580)
    twenty.filled = True
    twenty.fill_color = 'khaki'
    twenty.color = 'khaki'
    window.add(twenty)
    # the rest of the items consist the image on the invitation card


if __name__ == '__main__':
    main()
