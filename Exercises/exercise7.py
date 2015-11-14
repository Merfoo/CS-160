def main():
  winner = None
  while winner == None:
    print("Rock, paper, scissors!")
    p1_choice = get_player_input(1)
    p2_choice = get_player_input(2)
    winner = determine_winner(p1_choice, p2_choice)
    if winner == None:
      print("It's a tie!")
  print("Player "+str(winner)+" won!")

#get_player_input function goes here
def get_player_input(player):
	validInput = ["rock", "paper", "scissors"]
	user = input('Enter hand type player ' + str(player) \
				+ ' ("rock", "paper", "scissors"): ')

	while True:
		for i in range(len(validInput)):
			if user.lower() == validInput[i]:
				return i

		user = input("Enter valid hand type: ")
	
#determine_winner function goes here
def determine_winner(p1_choice, p2_choice):
	if p1_choice == p2_choice:
		return None
	
	if (p1_choice - 1) % 3 == p2_choice:	
		return 1 # Player 1

	return 2 # Player 2

main()
