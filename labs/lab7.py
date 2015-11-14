#!/usr/bin/env python3

def get_user_input():
	return input("Enter a string: ")

def num_matching_chars(strA, strB):
	biggerStr = strA
	smallerStr = strB

	if len(strA) < len(strB):
		biggerStr = strB
		smallerStr = strA

	charMatching = 0
	
	for i in range(len(smallerStr)):
		if smallerStr[i] == biggerStr[i]:
			charMatching += 1
	
	return charMatching

def percent_matching(strA, strB):
	lenA = len(strA)
	lenB = len(strB)
	biggerLen = lenA

	if lenB > biggerLen:
		biggerLen = lenB

	return num_matching_chars(strA, strB) / biggerLen

def main():
	strA = get_user_input()
	strB = get_user_input()

	if len(strA) == 0 and len(strB) == 0:
		print("No empty strings please")
		return

	print(str(percent_matching(strA, strB) * 100) + "% of the characters match")
	print(str(num_matching_chars(strA, strB)) + " characters match")

if __name__ == "__main__":
	main()
