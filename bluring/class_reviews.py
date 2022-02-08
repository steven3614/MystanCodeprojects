"""
File: class_reviews.py
Name:張文銓
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""
EXIT = '-100'


def main():
    """
    TODO: this function calculate the maximum and minimum and average grades of the SC001 and SC101.
    """
    maximum = -10
    maximum_1 = -10
    minimum = 2000
    minimum_1 = 2000
    sum_ = 0
    sum_1 = 0
    numbers = 0
    numbers_1 = 0
    # these variables storage the value of maximum, minimum and calculate the average
    # "maximum", "minimum", "sum_" and "numbers" is for SC001
    # "maximum_1", "minimum_1", "sum_1" and "numbers_1" is for SC101
    while True:
        class_number = input("Which class? ")
        if class_number == EXIT:
            break
        new_class = ""
        for i in range(len(class_number)):
            char = class_number[i]
            if char.islower:
                new_class += char.upper()
            else:
                new_class += char
        if new_class == 'SC001':
            score = int(input('Score: '))
            sum_ = sum_ + score
            numbers = numbers + 1
            if score > maximum:
                maximum = score
            if score < minimum:
                minimum = score
        if new_class == 'SC101':
            score_1 = int(input('Score: '))
            sum_1 = sum_1 + score_1
            numbers_1 = numbers_1 + 1
            if score_1 > maximum_1:
                maximum_1 = score_1
            if score_1 < minimum_1:
                minimum_1 = score_1
    if maximum == -10 and minimum == 2000 and maximum_1 == -10 and minimum_1 == 2000:
        print('No class scores were entered')
    else:
        print('=============SC001=============')
        if maximum == -10 and minimum == 2000:
            print('No score for SC001')
        else:
            print('Max(001): ' + str(maximum))
            print('Min(001): ' + str(minimum))
            print('Avg(001): ' + str(sum_ / numbers))
        print('=============SC101=============')
        if maximum_1 == -10 and minimum_1 == 2000:
            print('No score for SC101')
        else:
            print('Max(101): ' + str(maximum_1))
            print('Min(101): ' + str(minimum_1))
            print('Avg(101): ' + str(sum_1 / numbers_1))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #
if __name__ == '__main__':
    main()
