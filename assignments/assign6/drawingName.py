#!/usr/bin/env python3

################################################################################
# Program Filename: drawingName.py
# Author: Fauzi Kliman
# Date: 11/8/15
# Description: Draws text onto screen using turtle
# Input: Text to draw onto the screen
# Output: Text on the screen specified by user input
################################################################################

import turtle

class Letter:
	def __init__(self, letter):
		self.letter = letter
		self.pos = []

letters = {}

def createLetters():
	global letters
	
	l = Letter('A')
	l.pos.append([00.0, 00.0])
	l.pos.append([13.0, 26.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([19.5, 13.5])
	l.pos.append([06.5, 13.5])
	l.pos.append([26.0, 00.0])
	letters['A'] = l;

	l = Letter('B')
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 13.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([13.0, 26.0])
	l.pos.append([13.0, 13.0])	
	l.pos.append([00.0, 13.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['B'] = l

	l = Letter('C')
	l.pos.append([26.0, 26.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['C'] = l

	l = Letter('D')
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 13.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['D'] = l

	l = Letter('E')
	l.pos.append([26.0, 00.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([13.0, 13.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['E'] = l

	l = Letter('F')
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([13.0, 13.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['F'] = l

	l = Letter('G')
	l.pos.append([26.0, 26.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 13.0])
	l.pos.append([13.0, 13.0])
	l.pos.append([26.0, 00.0])
	letters['G'] = l

	l = Letter('H')
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 13.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['H'] = l

	l = Letter('I')
	l.pos.append([26.0, 26.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([13.0, 26.0])
	l.pos.append([13.0, 00.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['I'] = l

	l = Letter('J')
	l.pos.append([26.0, 26.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([13.0, 26.0])
	l.pos.append([13.0, 00.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['J'] = l

	l = Letter('K')
	l.pos.append([26.0, 26.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['K'] = l

	l = Letter('L')
	l.pos.append([00.0, 26.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['L'] = l

	l = Letter('M')
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([13.0, 00.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['M'] = l


	l = Letter('N')
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['N'] = l

	l = Letter('O')
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['O'] = l

	l = Letter('P')
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 13.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([26.0, 00.0])
	letters['P'] = l

	l = Letter('Q')
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([20.0, 06.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['Q'] = l

	l = Letter('R')
	l.pos.append([00.0, 00.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 13.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['R'] = l

	l = Letter('S')
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 13.0])
	l.pos.append([00.0, 13.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['S'] = l

	l = Letter('T')
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([13.0, 26.0])
	l.pos.append([13.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['T'] = l

	l = Letter('U')
	l.pos.append([00.0, 26.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['U'] = l

	l = Letter('V')
	l.pos.append([00.0, 26.0])
	l.pos.append([13.0, 00.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['V'] = l

	l = Letter('W')
	l.pos.append([00.0, 26.0])
	l.pos.append([06.5, 00.0])
	l.pos.append([13.0, 26.0])
	l.pos.append([19.5, 00.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['W'] = l

	l = Letter('X')
	l.pos.append([26.0, 26.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([13.0, 13.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['X'] = l

	l = Letter('Y')
	l.pos.append([13.0, 00.0])
	l.pos.append([13.0, 13.0])
	l.pos.append([00.0, 26.0])
	l.pos.append([13.0, 13.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([26.0, 00.0])
	letters['Y'] = l

	l = Letter('Z')
	l.pos.append([00.0, 26.0])
	l.pos.append([26.0, 26.0])
	l.pos.append([00.0, 00.0])
	l.pos.append([26.0, 00.0])
	l.pos.append([26.0, 00.0])
	letters['Z'] = l

turtleBusy = False

def draw(turtleT, text):
	global turtleBusy

	if turtleBusy:
		print("Drawing operation in progress!")
		return

	turtleBusy = True	
	turtleT.clear()

	width = (26 + 5) * len(text)
	startPos = [-(width / 2), 0]
	letterSpace = 5.0
	spaceSpace = 26.0
	turtleT.penup()	

	for c in text:
		maxX = 0.0

		if c == ' ':
			startPos[0] += spaceSpace

		else:
			for letterI in range(len(letters[c].pos)):
				if letterI == 1:
					turtleT.pendown()			

				if letterI == len(letters[c].pos) - 1:
					turtleT.penup()

				x = letters[c].pos[letterI][0]
				y = letters[c].pos[letterI][1]
				turtleT.setpos(x + startPos[0], y + startPos[1])
		
				if x > maxX:
					maxX = x
			
		startPos[0] += letterSpace + maxX	
	
	turtleBusy = False

def main():
	w = turtle.Screen()
	t = turtle.Turtle()
	t.pensize(2)

	createLetters()
	
	text = ""
	w.onclick(lambda x, y: draw(t, text))

	while True:
		prompt = input("Text to be drawn or 'q' to quit: ")
		
		if prompt == 'q':
			return
		
		invalidInput = False

		for c in prompt:
			if (c < 'A' or  c > 'Z') and c != ' ':
				print("Uppercase letters and spaces only!")
				invalidInput = True
				break
		
		if not invalidInput:
			text = prompt
			draw(t, text)

if __name__ == "__main__":
	main()
