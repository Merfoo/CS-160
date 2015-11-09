################################################################################
# Program Filename: assign3.py
# Author: Fauzi Kliman
# Date: 10/18/15
# Description: Basic calculator in python for two numbers a number operation
# Input: A number  operation, two numbers, input to continue or quit calculator 
# Output: The result of the chosen number operation executed on the two numbers
################################################################################


################################################################################
# Function: main
# Description: Function that gets called upon the execution of this script
# Parameters: None
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def main():

	# Loop program until user requests to quit
	while True:

		# Ask user for number operation, looping until operation is valid
		while True:
			validOperations = ["+", "-", "/", "*", "**", "%"]
			operation = input("Enter a number operation (+, -, /, *, **, %): ")
		
			try:
				validOperations.index(operation)
				break	
		
			except ValueError:
				print("Invalid number operation!")

		# Ask user for first number, looping until number is valid
		while True:
			try:
				firstNum = int(input("Enter your first number: "))
				break

			except ValueError:
				print("Invalid number!")		

		# Ask user for second number, looping until number is valid
		while True:
			try:	
				secondNum = int(input("Enter your second number: "))
				break

			except ValueError:
				print("Invalid number!")

		if (operation == '/' or operation == '%') and secondNum == 0:
			print("Can't divide by 0!")

		elif operation == '+':
			print(firstNum + secondNum)
	
		elif operation == '-':
			print(firstNum - secondNum)
	
		elif operation == '/':
			print(firstNum / secondNum)

		elif operation == '*':
			print(firstNum * secondNum)

		elif operation == "**":
			print(firstNum ** secondNum)

		elif operation == '%':
			print(firstNum % secondNum)

		# Ask user to continue using calculator, looping until valid input
		while True:	
			playAgain = input("Would you like to play again? (0 - no, 1 - yes): ")
	
			if playAgain == '0':
				print("\n\nThanks for using this calculator.")
				return
		
			elif playAgain == "1":
				print("\n")
				break
		
			else:
				print("Invalid option!")


if __name__ == "__main__":
	main()
