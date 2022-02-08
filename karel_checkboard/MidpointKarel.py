from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: steven
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    karel will fill in the first line with beepers and pick up
    beepers from the sides, gradually there will only be one beeper left
    and that one is the mid point.
    """
    fill_in()
    go_back()
    picking_beepers()
    find_that_beeper()


def fill_in():
    """
    pre-condition: karel is at(1,1) facing east.
    post-condition: karel is at the very right of the first line and
    filled in beepers in every point of the first line.
    """
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()


def go_back():
    """
    pre-condition: karel is at the very right of the line facing east.
    post-condition: karel is at the very left of the line and facing east.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()


def picking_beepers():
    """
    pre-condition:karel is at the original position and facing east.
    post-condition: karel is at the mid point with a beeper.
    """
    while front_is_clear():
        while on_beeper():
            move()
            if on_beeper():
                turn_around()
                move()
                pick_beeper()
                go_back()
        if front_is_clear():
            move()
    turn_around()


def find_that_beeper():
    """
    pre-condition:karel is at the side of the line and facing the only beeper.
    post-condition:karel is standing on that only beeper and that is the mid o[point.
    """
    while not on_beeper():
        move()
    pass


def turn_around():
    # definite turning around by turning left twice.
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
