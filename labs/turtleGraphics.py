import turtle

def getIntInput(inputStr, errStr, minVal):
	userInput = minVal

	while True:
		try:
			userInput = int(input(inputStr))
		
		except ValueError:
			userInput = minVal

		if userInput <= minVal:
			print(errStr)
		
		else:
			return userInput
	
def main():
	print("Turtle Graphics Yo!")
	window = turtle.Screen()
	myTurtle = turtle.Turtle()

	while True:	
		sideNum = getIntInput("Enter sides: ", "Invalid side number!", 2)
		sideLen = getIntInput("Enter side length: ", "Invalid side length!", 0)
		angPerSide = (360 / sideNum)
	
		for side in range(sideNum):
			myTurtle.forward(sideLen)
			myTurtle.left(angPerSide)		
		
		while True:
			quit = input("1 to quit, 0 to continue: ")

			if quit == '1':
				return
			
			elif quit == '0':
				break
			
			print("Invalid input!")
	
		#window.mainloop()

if __name__ == "__main__":
	main()
