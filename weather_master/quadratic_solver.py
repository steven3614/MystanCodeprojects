"""
File: quadratic_solver.py
Name:張文銓
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    """
    This function helps user to check if an equation has one real root, two real roots or no real root
    and also calculate the roots if it has real roots.
    """
    print("stanCode Quadratic Solver!")
    a = int(input(""))
    b = int(input(""))
    c = int(input(""))
    discriminant = b ** 2 - (4 * a * c)
    # discriminant is a equation that help user to check how many real roots are there.
    if discriminant > 0:
        # the situation when the equation has two real roots
        x = ((-b) + math.sqrt(discriminant)) / 2
        y = ((-b) - math.sqrt(discriminant)) / 2
        print("Two roots: " + str(x) + ", " + str(y))
    elif discriminant == 0:
        # the situation when the equation has one root
        x = ((-b) + math.sqrt(discriminant)) / 2
        print("One root: " + str(x))
    elif discriminant < 0:
        # the situation when the equation has no real roots
        print("No real roots")


# DO NOT EDIT CODE BELOW THIS LINE #
if __name__ == "__main__":
    main()
