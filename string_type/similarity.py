"""
File: similarity.py
Name: 張文銓
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    This function compare two DNA sequences and find the highest similarity.
    """
    data()


def data():
    # input the DNA sequence and upper it
    long_sequence = input("Please give me a DNA sequence to search: ")
    new_long = ""
    for i in range(len(long_sequence)):
        char = long_sequence[i]
        if char.islower:
            new_long += char.upper()
        else:
            new_long += char
    # input the DNA sequence to match and upper it
    short_sequence = input("What DNA sequence would you like to match? ")
    new_short = ""
    for i in range(len(short_sequence)):
        char = short_sequence[i]
        if char.islower:
            new_short += char.upper()
        else:
            new_short += char
    times = int(len(new_long)) - int(len(new_short)) + 1
    # 'times' is a variable that calculate the total times that need to match
    maximum = 0
    similar = ''
    for i in range(times):
        same = 0
        # 'same' is a variable that count the times that the DNA is match in the sequence
        for j in range(len(new_short)):
            char_short = new_short[j]
            char_long = new_long[j+i]
            if char_long == char_short:
                same += 1
            percentage = same / len(new_short)
            if percentage > maximum:
                maximum = percentage
                similar = new_long[i: i+len(new_short)]
    print("The best match is " + similar)


# DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
