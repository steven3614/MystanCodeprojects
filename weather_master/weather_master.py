"""
File: weather_master.py
Name:張文銓
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100
# -100 is the number that will break the function and show the output.


def main():
	"""
	This function help user to check out the weather, it will shows the highest, the lowest temperature,
	the average temperature and how many cold days.
	"""
	print('stanCode \"Weather Master 4.0\"!')
	data = int(input('Next Temperature: (or -100 to quit)? '))
	if data == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = data
		minimum = data
		cold_day = 0
		# "cold_day" is a variable that count how many days are below 16 degree which will be consider as "cold days".
		numbers = 0
		# "numbers" is a variable that count how many days are there in order to calculate the average temperature.
		sum_ = 0
		sum_ = sum_ + data
		# "sum_" is a variable that calculate the sum of the temperature in order to calculate the average temperature.
		if data < 16:
			cold_day = cold_day + 1
		while True:
			data = int(input('Next Temperature: (or -100 to quit)? '))
			numbers = numbers + 1
			if data == EXIT:
				break
			sum_ = sum_ + data
			if data > maximum:
				maximum = data
			elif data < minimum:
				minimum = data
			if data < 16:
				cold_day = cold_day + 1
		print('Highest temperature = ' + str(maximum))
		print('Lowest temperature = ' + str(minimum))
		print('Average = ' + str(sum_ / numbers))
		print(str(cold_day) + ' cold day(s)')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
