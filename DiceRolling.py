import random

print(" ")
print("Calvins Dice Rolling")
print("Made on: 06/02/18")
print(" ")

running = True
	
while running:
	print("1 = 6-Sided Dice")
	print("2 = 10-Sided Dice")
	print("3 = 20-Sided Dice")
	print("4 = 100-Sided Madness!")
	print("5 = Exit!")
	print(" ")
	diceType = int(input("Please enter the number according to which Dice you would like to roll: "))
	if diceType == 1:
		result = random.randint(1,6)
		print(" ")
		print("You rolled a", result)
		print(" ")
	elif diceType == 2:
		result = random.randint(1,10)
		print(" ")
		print("You rolled a", result)
		print(" ")
	elif diceType == 3:
		result = random.randint(1,20)
		print(" ")
		print("You rolled a", result)
		print(" ")
	elif diceType == 4:
		result = random.randint(1,100)
		print(" ")
		print("You rolled a", result)
		print(" ")
	elif diceType == 5:
		print(" ")
		print("Ok, nevermind then!")
		print(" ")
		running = False