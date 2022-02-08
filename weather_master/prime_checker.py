"""
File: prime_checker.py
Name: 張文銓
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


EXIT = -1
# -1 is the number that will break the function and end the function.


def main():
	"""
	This function help user to check whether the number they entered is a prime or not.
	The definition of a prime is that a prime number is a number greater than 1 with
	only two factors – themselves and 1.
	"""

	print('Welcome to the prime checker!')
	while True:
		i = 2
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one!')
			break
		# I check it by using the number "n" to divide by 2 to n-1.
		while i < n:
			if n % i != 0:
				i = i + 1
			if i == n:
				print(str(n) + ' is a prime number.')
			elif n % i == 0:
				print(str(n) + ' is not a prime number.')
				break
				# break to avoid the infinite loop.


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()