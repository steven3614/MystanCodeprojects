"""
File: anagram.py
Name: 張文銓
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO: this function finds whether the words appears in the dictionary
    """
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    while True:
        word = input('Find anagrams for: ')
        # start = time.time()
        if word == EXIT:
            break
        else:
            print('Searching...')
            d = read_dictionary()
            find_anagrams(word, d)
    # end = time.time()
    # print('----------------------------------')
    # print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    lst = []
    with open(FILE, 'r') as f:
        for data in f:
            lst .append(data.split())
    return lst


def find_anagrams(s, d):
    """
    :param s: the word user want to find
    :return: the result of the finding
    """
    ans = ''
    idx_lst = []
    python_list = []
    helper(s, ans, idx_lst, python_list, d)
    print(python_list)


def helper(s, ans, idx_lst, python_list, d):
    if len(s) == 0:
        if ans in d:
            python_list.append(ans)
            print(f'Found:{ans}')
    else:
        for i in range(len(s)):
            if has_prefix(ans, idx_lst) is True:
                ans += s[i]
                idx_lst.append(i)
                helper(s, ans, idx_lst, python_list, d)
                idx_lst.pop()
                ans = ans[:-1]


def has_prefix(sub_s, lst):
    """
    :param sub_s: a part of the word s
    :return: whether the word is in the dictionary
    """
    for word in lst:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
