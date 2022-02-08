"""
File: boggle.py
Name: 張文銓
----------------------------------------
TODO: this function finds all the words that is longer than 4 letters in the boggle board.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO: this function let the user input the boggle board and fin the possible words in it
	"""
	start = time.time()
	d = read_dictionary()
	lst_big = []
	for i in range(4):
		letter = input(f'{i+1} row of letters: ')
		count = 0
		lst_small = []
		for j in range(len(letter)):
			if j % 2 == 0:
				lst_small.append(letter[j].lower())
			if letter[j].isalpha():
				count += 1
		lst_big.append(lst_small)
		if len(letter) != 7 or count != 4:
			print(f'Illegal input')
			break
	# everyone can be the head of the word
	counter = 0
	found = []
	for i in range(4):
		for j in range(4):
			s = lst_big[i][j]
			start_point = (i, j)
			path = [start_point]
			find_the_word(lst_big, d, s, start_point, found, path)
			# if find_the_word(i, j, lst_big[i][j]) not in read_dictionary() and has_prefix(lst_big[i][j]) is True:
			# 	print(f'Found: {find_the_word(i, j, lst_big[i][j])}')
			# 	counter += 1
	print(f'There are {len(found)} words in total')
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		all_words = []
		for line in f:
			all_words.append(line.strip())
	return all_words


def find_the_word(board, d, s, point, found, path):
	"""
	:param current_x: the x position of the board
	:param current_y: the y position of the board
	:param current_s: the current word string right now
	:return:
	"""
	# recursion finding neighbor
	if len(s) >= 4:
		if s in d and s not in found:
			found.append(s)
			print(f'Found: {s}')

	cur_i, cur_j = point
	for i in range(-1, 2):
		for j in range(-1, 2):
			next_i = cur_i + i
			next_j = cur_j + j
			if 0 <= next_i < 4 and 0 <= next_j < 4:
				if (next_i, next_j) not in path:
					s += board[next_i][next_j]
					path.append((next_i, next_j))
					if has_prefix(s, d):
						find_the_word(board, d, s, (next_i, next_j), found, path)
					path.pop()
					s = s[:-1]


def has_prefix(sub_s, d):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""

	for word in d:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
