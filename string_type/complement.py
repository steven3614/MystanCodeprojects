"""
File: complement.py
Name: 張文銓
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    build_complement()


def build_complement():
    d = input("Please give me a DNA strand and I'll find the complement: ")
    new_d = ""
    for i in range(len(d)):
        char = d[i]
        if char.islower:
            new_d += char.upper()
        else:
            new_d += char

    ans = ""
    for i in range(len(new_d)):
        char = new_d[i]
        if char == 'A':
            ans = ans + 'T'
        elif char == 'T':
            ans = ans + 'A'
        elif char == 'C':
            ans = ans + 'G'
        elif char == 'G':
            ans = ans + 'C'
    print("The complement of " + d + " is " + ans)


# DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
