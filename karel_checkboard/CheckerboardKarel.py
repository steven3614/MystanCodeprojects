from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: steven
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    break the behavior into fill in odd line, even line and the only row.
    karel will fill in the beepers differently while it is in the different line.
    """
    while front_is_clear():
        fill_odd_line()
        go_back()
        fill_even_line()
        go_back()
    only_row()


def fill_odd_line():
    """
    pre-condition: karel is at (1,1) facing east
    post-condition: karel is at the very right of the line and filled in beepers
    with one space between one another and turn around facing west(first point if filled in)
    """
    put_beeper()
    move()
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    turn_around()


def go_back():
    """
    pre-condition: karel is at the very right of the line facing west.
    post-condition:  karel is at the very left of the next line facing east.
    """
    while front_is_clear():
        move()
    turn_right()
    if front_is_clear():
        move()
        turn_right()


def fill_even_line():
    """
    pre-condition: karel is at the very left of the line and facing east.
    post-condition: karel is at the very right of the line and filled in beepers
    with one space between one another and turn around facing west(first point is not filled in)
    """
    while front_is_clear():
        move()
        put_beeper()
        if front_is_clear():
            move()
    turn_around()


def only_row():
    """
    when there is only one row for karel.
    """
    turn_left()
    if not left_is_clear():
        put_beeper()
        if front_is_clear():
            move()
        while front_is_clear():
            move()
            put_beeper()
            if front_is_clear():
                move()


def turn_around():
    # definite turning around by turning left twice.
    turn_left()
    turn_left()


def turn_right():
    """
    karel does not know how to turn right so we let it turn left three times
    in order to have the same result of turning right.
    """
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
