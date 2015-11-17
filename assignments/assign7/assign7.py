#!/usr/bin/env python3

################################################################################
# Program Filename: assign7.py
# Author: Fauzi Kliman
# Date: 11/15/15
# Description: Calculates numeric grade in a class based on scores and weights
# Input: None: Number of tests, assignments, exercises, labs, weight for final 
#              if different, weight for each, scores for each
# Ouput: None: Grade in classs
################################################################################


################################################################################
# Function: calculate_sum()
# Description: Calculates the sum of an array for numbers
# Parameters: List of numbers
# Return Values: Sum of list of numbers
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def calculate_sum(nums):
	total = 0
	
	for val in nums:
		total += val

	return total


################################################################################
# Function: get_initial_input()
# Description: Asks the user for the amount of tests, assignments, exercises and#			   labs in their course
# Parameters: List containings the name for each amount of something
# Return values: List containing amount tests, assignments, exercises and labs
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def get_initial_input(nameForEach):
	numForEach = [0 for i in range(len(nameForEach))]
	
	for i in range(len(numForEach)):
		num = -1
	
		while True:
			try:
				num = int(input("Number of " + nameForEach[i] + ": "))

				if num >= 0:
					break
			
			except ValueError:
				pass
		
			print("Invalid number!")

		numForEach[i] = num

	return numForEach


################################################################################
# Function: get_scores()
# Description: Asks the user for all the scores
# Parameters: Name for current scores, Number of scores to ask the user for
# Return values: List of scores
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def get_scores(name, amount):
	scores = [0 for i in range(amount)]

	for i in range(amount):
		score = -1

		while True:
			try:
				display = "The " + name + " score " + str(i + 1) + ": "
				score = float(input(display))
				
				if score >= 0:
					break
		
			except ValueError:
				pass

			print("Invalid score!")

		scores[i] = score

	return scores		


################################################################################
# Function: get_weights()
# Description: Gets the weights for all the categories if amount is > 0
# Parameters: Name of each category, amount for each category
# Return values: List of weights for each category
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def get_weights(nameForEach, amountForEach):
	weightSum = 0.0
	weightForEach = [0.0 for i in range(len(nameForEach))]

	while True:
		weightSum = 0.0
		validWeightSum = True

		for i in range(len(nameForEach)):
			if amountForEach[i] == 0:
				continue

			weight = -1.0

			while True:
				try:
					display = "Weight for " + nameForEach[i] + " : "
					weight = float(input(display))

					if weight > 0.0:
						break

				except ValueError:
					pass

				print("Invalid weight!")

			weight /= 100.0
			weightSum += weight

			if weightSum > 1.0:
				validWeightSum = False
				break

			weightForEach[i] = weight

		if validWeightSum and weightSum == 1.0:
			break

		print("The weight must sum to exactly 100.0, not over, not under!")

	return weightForEach


################################################################################
# Function: calculate_weighted_avg()
# Description: Calculates the average of a list of scores and multiplies it by
#              a weight constant
# Parameters: Weight constant, list of scores
# Return values: Weighted avg of scores
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def calculate_weighted_avg(weight, scores):
	total = calculate_sum(scores)
	return (total / len(scores)) * weight


################################################################################
# Function: calculate_weighted_sum()
# Description: Calculates the sum of a list of scores and multiplies it by a 
#              weight constant
# Parameters: Weight constant, list of scores
# Return values: Weighted sum of scores 
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def calculate_weighted_sum(weight, scores):
	total = calculate_sum(scores)
	return total * weight


################################################################################
# Function: calculate_class_grade()
# Description: Calculates the class grade by summing the values in the list of
#              grades
# Parameters: List of grades
# Return values: Sum of list of grades
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def calculate_class_grade(gradeForEach):
	grade = calculate_sum(gradeForEach)
	return grade


################################################################################
# Function: main()
# Description: Entry point for grade calculator
# Parameters: None
# Return Values: None
# Pre-Conditions: None
# Post-Conditions: None
################################################################################
def main():
	nameForEach = ["tests", "assignments", "exercises", "labs"]
	
	while True:
		amountForEach = get_initial_input(nameForEach)	
		weightForEach = get_weights(nameForEach, amountForEach)
		gradeForEach = [0 for i in range(len(amountForEach))]
		finalWeight = -1.0;
		
		if amountForEach[0] > 0:
			while True:
				try:
					display = "Weight for Final (-1 if same as tests): "	
					finalWeight = float(input(display))

					if finalWeight == -1.0 or finalWeight > 0:
						break

				except ValueError:
					pass
		
				print("Invalid Weight!")

		for i in range(len(amountForEach)):
			if amountForEach[i] == 0:
				continue
		
			weight = weightForEach[i]
			scores = get_scores(nameForEach[i], amountForEach[i])
			grade = 0

			if nameForEach[i] == "labs":
				grade = calculate_weighted_sum(weight, scores)
	
			elif nameForEach[i] == "tests":
				if finalWeight != -1.0:
					testGrade = 0
					finalGrade = scores[-1] * finalWeight

					if len(scores) > 1:
						testScores = scores[:len(scores) - 2]
						testGrade = calculate_weighted_avg(weight, testScores)

					grade = finalGrade + testGrade
			
				else:
					grade = calculate_weighted_avg(weight, scores)

			else:
				grade = calculate_weighted_avg(weight, scores)

			gradeForEach[i] = grade
	
		classGrade = calculate_class_grade(gradeForEach)
		print("Grade for the class: " + str(classGrade))
		
		while True:
			quit = input("Calculate grade for another class? (yes/no): ")

			if quit == "yes":
				break

			if quit == "no":
				return

			print("Invalid response!")

if __name__ == "__main__":
	main()
