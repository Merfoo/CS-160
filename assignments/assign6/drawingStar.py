#!/usr/bin/env python3

################################################################################
# Program Filename: drawingStar.py
# Author: Fauzi Kliman
# Date: 11/8/15
# Description: Draws a user specified shape, redrawing it if screen is clicked
# Input: Number of sides to draw
# Output: The shape based on the number of sides specified
################################################################################

import turtle

turtleBusy = False

def draw(turtleT, sides, sideLen):
		global turtleBusy

		if turtleBusy:
			print("A drawing operation is already in progress")		
			return

		turtleBusy = True
		turtleT.clear()
	
		ang = 2 * (360 / sides)
		fwd = sideLen

		turtleT.setpos(fwd / 2, 0)
		turtleT.setheading(180)
	
		for x in range(sides):
			turtleT.forward(fwd)
			turtleT.left(ang)
		
		turtleBusy = False

def main():
	w = turtle.Screen()	
	t = turtle.Turtle()
	defaultSides = 5
	sides = defaultSides
	sideLen = 100
	w.onclick(lambda x, y: draw(t, sides, sideLen))	

	while True:
		while True:
			prompt = input("Enter amount of sides or 'q' to quit: ")
					
			if prompt[0] == 'q':
				return

			try:
				sides = int(prompt)
	
				if sides > 3:
					break

			except ValueError:
				pass
				
			print("Invalid amount of sides!")
			sides = defaultSides		

		draw(t, sides, sideLen)
		
if __name__ == "__main__":
	main()
