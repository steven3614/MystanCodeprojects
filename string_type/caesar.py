"""
File: caesar.py
Name: 張文銓
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This function is a function that let user know the password by knowing a secret number and a string that is
    none sense.
    """
    deciphered()


def deciphered():
    number = input("Secret number: ")  # this is the secret number that let user know how many spaces they need to move.
    ciphered = input("What's the ciphered string? ")  # the none sense string
    new_ciphered = ""  # let the string be upper case if it is not.
    for i in range(len(ciphered)):
        char = ciphered[i]
        if char.islower:
            new_ciphered += char.upper()
        else:
            new_ciphered += char
    new_number = 26 - int(number)
    new_alphabet = ALPHABET[int(new_number):] + ALPHABET[:int(new_number)]
    # reassign the alphabet to a new order
    decipher = ""
    for i in range(len(new_ciphered)):
        char = new_ciphered[i]
        final = new_alphabet.find(char)
        if final == -1:
            decipher += char
        else:
            decipher += ALPHABET[int(final)]
    print("The deciphered string is: " + str(decipher), end="")


# DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
