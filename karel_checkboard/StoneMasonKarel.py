from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: steven
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    let turning left, fill in and go to the next stop be a set for karel. However, this set is not suitable
    for the last one. karel will run into the wall if we use the same set. Thus, using while to discriminate
    the last set and the others. When karel notice that it is at the last let, it will stop when it finish fill
    in.
    """
    while front_is_clear():
        turn_left()
        fill_in()
        go_back()
        # go back to the position and face east, same as the original situation.
        go_next()
        # go to the next stop and facing east.
    turn_left()
    fill_in()
    go_back()


def fill_in():
    """
    pre-condition: karel is at the bottom of the row and facing north.
    post-condition: karel is at the top of the row and filled in that row.
    """
    while front_is_clear():
        if on_beeper():
            move()
        else:
            put_beeper()
            move()
    if on_beeper():
        pass
    else:
        put_beeper()


def go_back():
    """
    pre-condition: karel is at the top of the row facing north.
    post-condition: karel is at the bottom of the row facing east.
    """
    turn_around()
    while front_is_clear():
        move()
    turn_left()


def turn_around():
    # define turning around as turning left twice.
    turn_left()
    turn_left()


def go_next():
    # move to the next pillar facing east, the space between every two pillars is same.
    move()
    move()
    move()
    move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
