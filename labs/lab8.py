scoreLen = int(input("Number of scores: "))
scores = [0] * scoreLen

for i in range(scoreLen):
	scores[i] = int(input("Score " + str(i + 1) + ": "))

scores.sort()
print(scores)
print(sum(scores) / scoreLen)
