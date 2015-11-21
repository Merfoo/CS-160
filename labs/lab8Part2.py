amountOfNums = int(input("Number of numbers: "))
array = [1, 2, 3, 4, 5]

for i in range(amountOfNums):
	user = int(input("Number " + str(i + 1) + ": "))
	append = True

	for num in array:
		if user == num:
			append = False
			break

	if append:
		array.append(user)

print(array)
