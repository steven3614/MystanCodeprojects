"""
File: coin_flip_runs.py
Name:張文銓
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	TODO: this function show all the result of the times that have the same result in a row as the user input.
	"""
	print('Let\'s flip a coin!')
	numbers = int(input('Number of runs: '))
	same = 0
	# the variable "same" counts the times of the same result in a row
	b = 0
	while True:
		num = r.randrange(1, 3)
		# num randomly choose a number between 1 and 2
		if num == 1:
			num = 'H'
		else:
			num = 'T'
		# this if and else change 1 and 2 into H and T
		print(str(num), end='')
		if (num == b) and (b != c):
			same += 1
		c = b
		b = num
		# b and c are the variables that help checking if the result is three(or more) in a row or not.
		if same == numbers:
			break


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #
if __name__ == "__main__":
	main()
