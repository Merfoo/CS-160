while True:
	operation = input("Enter a number operation (+, -, /, *, **, %): ")
	firstNum = int(input("Enter your first number: "))
	secondNum = int(input("Enter your second number: "))
	
	if operation == '+':
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
	
	playAgain = input("Would you like to play again? (0 - no, 1 - yes): ")
	
	if playAgain == '0':
		break

print("Thanks for using this calculator.")
