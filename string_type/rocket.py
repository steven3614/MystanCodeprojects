"""
File: rocket.py
Name: 張文銓
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
	"""
	this function create a rocket with different symbol.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()


def head():
	# create the head of the rocket
	for i in range(SIZE):
		space = SIZE - (i + 1)
		for k in range(space+1, 0, -1):
			print(" ", end="")
		for j in range(i + 1):
			print("/", end="")
		for j in range(i + 1):
			print("\\", end="")
		print("")


def belt():
	# create the belt of the rocket
	print("+", end="")
	for i in range(SIZE*2):
		print("=", end="")
	print("+", end="")
	print("")


def upper():
	# create the upper body of the rocket
	for i in range(SIZE):
		print("|", end="")
		dot = SIZE - (i+1)
		for k in range(dot, 0, -1):
			print(".", end="")
		for j in range(i + 1):
			print("/", end="")
			print("\\", end="")
		for k in range(dot, 0, -1):
			print(".", end="")
		print("|", end="")
		print("")


def lower():
	# create the lower body of the rocket
	for i in range(SIZE):
		size = SIZE-i
		print("|", end="")
		for j in range(i):
			print(".", end="")
		for k in range(size, 0, -1):
			print("\\", end="")
			print("/", end="")
		for j in range(i):
			print(".", end="")
		print("|", end="")
		print("")


# DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()