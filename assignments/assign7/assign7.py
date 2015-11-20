#!/usr/bin/env python3

################################################################################
# Program Filename: assign7.py
# Author: Fauzi Kliman
# Date: 11/15/15
# Description: Calculates numeric grade in a class based on scores and weights
# Input: Number of finals, tests, assignments, exercises, labs, weight for each,
#        scores for each
# Ouput: Grade in classs
################################################################################


################################################################################
# Function: calculate_sum()
# Description: Calculates the sum of an array for numbers
# Parameters: List of numbers
# Return Values: Sum of list of numbers
# Pre-Conditions: nums should contain a list of numbers
# Post-Conditions: Return the sum of all the values in the list
################################################################################
def calculate_sum(nums):
    total = 0.0
    
    for val in nums:
        total += val

    return total


################################################################################
# Function: get_int_input()
# Description: Gets a valid int response from the user
# Parameters: The string to display when asking for input
# Return values: An int
# Pre-Conditions: None
# Post-Conditions: Return a valid int
################################################################################
def get_int_input(display):
    while True:
        try:
            response = int(input(display))
            return response

        except ValueError:
            print("Invalid number!")


################################################################################
# Function: get_int_input()
# Description: Gets a valid float  response from the user
# Parameters: The string to display when asking for input
# Return values: An float
# Pre-Conditions: None
# Post-Conditions: Return a valid float
################################################################################
def get_float_input(display):
    while True:
        try:
            response = float(input(display))
            return response

        except ValueError:
            print("Invalid number!")


################################################################################
# Function: get_initial_input()
# Description: Asks the user for the amount of tests, assignments, exercises and
#              labs in their course
# Parameters: List containings the name for each amount of something
# Return values: List containing amount finals,  tests, assignments, exercises
#                and labs
# Pre-Conditions: The names of all the categories
# Post-Conditions: Return a list
################################################################################
def get_initial_input(nameForEach):
    numForEach = [0] * len(nameForEach)
    
    for i in range(len(numForEach)):
        num = -1
    
        while True:
            num = get_int_input("Number of " + nameForEach[i] + "s: ")

            if num >= 0:
                break

            print("Invalid number of " + nameForEach[i] + "s!")

        numForEach[i] = num

    return numForEach


################################################################################
# Function: get_scores()
# Description: Asks the user for all the scores
# Parameters: Name for current scores, number of scores to ask the user for
# Return values: List of scores
# Pre-Conditions: Name for current category, amount >= 0
# Post-Conditions: Return list of scores >= 0
################################################################################
def get_scores(name, amount):
    scores = [0] * amount

    for i in range(amount):
        score = -1.0

        while True:
            display = "Score for " + name + " " + str(i + 1) + ": "
            score = get_float_input(display)

            if score >= 0:
                break

            print("Invalid score!")

        scores[i] = score

    return scores       


################################################################################
# Function: get_weights()
# Description: Gets the weights for all the categories if amount is > 0
# Parameters: Name of each category, amount for each category
# Return values: List of weights for each category
# Pre-Conditions: Name of each category, amount of each >= 0
# Post-Conditions: List of weights that sum to 1.0
################################################################################
def get_weights(nameForEach, amountForEach):
    weightSum = 0.0
    weightForEach = [0.0] * len(nameForEach)

    while True:
        weightSum = 0.0
        validWeightSum = True

        for i in range(len(nameForEach)):
            if amountForEach[i] == 0:
                continue

            weight = -1.0

            while True:
                display = "Weight for " + nameForEach[i] + "s: "
                weight = get_float_input(display)

                if weight > 0.0:
                    break

                print("Invalid weight!")

            weight /= 100.0
            weightSum += weight

            if weightSum > 1.0:
                validWeightSum = False
                break

            weightForEach[i] = weight

        if validWeightSum and weightSum == 1.0:
            break

        print("The weights must sum to 100!")

    return weightForEach


################################################################################
# Function: calculate_weighted_avg()
# Description: Calculates the average of a list of scores and multiplies it by
#              a weight constant
# Parameters: Weight constant, list of scores
# Return values: Weighted avg of scores
# Pre-Conditions: Weight > 0, scores >= 0
# Post-Conditions: Average >= 0
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
# Pre-Conditions: Weight > 0, scores >= 0
# Post-Conditions: Sum >= 0
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
# Pre-Conditions: Grade for each category >= 0
# Post-Conditions: Class grade >= 0
################################################################################
def calculate_class_grade(gradeForEach):
    grade = calculate_sum(gradeForEach)
    grade = (((grade + 0.005) * 100) // 1) / 100
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
    nameForEach = ["final", "test", "assignment", "exercise", "lab"]
    
    while True:
        amountForEach = get_initial_input(nameForEach)  
        weightForEach = get_weights(nameForEach, amountForEach)
        gradeForEach = [0] * len(amountForEach)

        for i in range(len(amountForEach)):
            if amountForEach[i] == 0:
                continue
        
            weight = weightForEach[i]
            scores = get_scores(nameForEach[i], amountForEach[i])
            grade = 0

            if nameForEach[i] == "labs":
                grade = calculate_weighted_sum(weight, scores)
    
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
