from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: steven
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Karel's two main behaviors is to go to the position of the newspaper
    and pick it up and then go back to the original position.
    """
    move_to_newspaper()
    pick_go_back()


def move_to_newspaper():
    """
    pre-condition: karel is at the original position and facing east.
    post-condition:karel is on the newspaper(beeper)facing east.
    """
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def pick_go_back():
    """
    pre-condition:karel picked up the newspaper
    post-condition:karel is at the original position and facing east.
    """
    pick_beeper()
    turn_around()
    move()
    move()
    move()
    turn_right()
    move()
    turn_right()
    put_beeper()


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
