################################################################################
# Program Filename: assign4.py
# Author: Fauzi Kliman
# Date: 10/31/15
# Description: Takes in a positive whole number n and outputs its square root
# using the Babylonian algorithm
# Input: A positive whole number n
# Output: The square root of input n
################################################################################

import math

def main():
	n = -1

	while True:
		try:
			n = int(input("Positive whole number to take square root of: "))
	
		except ValueError:
			pass
	
		if n >= 0:
			break

		print("Invalid number!")
	
	guess = 0

	if n == 0 or n == 1:
		guess = n
	
	else:
		guess = n / 2
		prevGuess = guess
		deltaG = 0.00000001
	
		while True:
			r = n / guess
			guess = (guess + r) / 2
		
			if abs(guess - prevGuess) < deltaG:
				break 
		
			prevGuess = guess
	
	print("Square root of " + str(n) + " is " + str(guess))
	print("The sqrt function returns " + str(math.sqrt(n)))

if __name__ == "__main__":
	main()
