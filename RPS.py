import random


print("welcome to the wizard remod of nifemi RPS game\nEnter R,P or S")

# list of user wins, list of robot wins
who_wins = [['RS','PR','SP'],['RP','PS','SR']]


ai = False
ai_control = input("\nenable ai (yes or no)\n>> ")

if ai_control == "yes":
	learnt_moves = {}
	ai = True
	
while True:
	playable = ["R", "P","S"]
	user_pick = input("\nplayer: ").upper().strip()
	if user_pick in playable:
		if ai == False:
			wizard_choice = random.choice(playable)
		elif ai == True:
			for guess_choice in playable:
				if user_pick + guess_choice in learnt_moves:
					
					if learnt_moves[user_pick + guess_choice] == "wizard_wins":
						wizard_choice = guess_choice
						break
						
					if learnt_moves[user_pick + guess_choice] == "player_wins":
						playable.remove(guess_choice)
						
					if learnt_moves[user_pick + guess_choice] == "draw":
						playable.remove(guess_choice)
						
						
				else:
					wizard_choice = random.choice(playable)
					
		print(f"wizard: {wizard_choice} ")
		played = user_pick + wizard_choice
		ai_condition = (ai == True) and (played not in learnt_moves)
		if played in who_wins[0]:
			print("player wins")
			if ai_condition:
				learnt_moves[played] = "player_wins"
				print(learnt_moves)
				
		elif played  in who_wins[1]:
			print("wizard wins")
			if ai_condition:
				learnt_moves[played] = "wizard_wins"
				print(learnt_moves)
				
		else:
			print('draw')	
			if ai_condition:
				learnt_moves[played] = "draw"
				print(learnt_moves)
	elif user_pick == "Q":
		break
	else:
		print('invalid choice')
	
	








