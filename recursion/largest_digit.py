"""
File: largest_digit.py
Name: 張文銓
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: n is a integer that the user want to find the biggest number in it
	:return: return the biggest number in the integer.
	"""

	if n < 0:				# if the integer in negative, we need to turn it to positive first.
		n = -n
	if n == 0:				# if n == 0, means that the function had finished comparing the numbers.
		return n
	else:
		digit = n % 10
		return max(find_largest_digit(n // 10), digit)



if __name__ == '__main__':
	main()
