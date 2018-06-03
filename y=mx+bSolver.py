print(" ")
print("Y=Mx+B Calculator")
print("Made on 06/02/18")
print(" ")

running = True

while running:
	print(" ")
	print("Equation form: Y = Mx + B")
	print(" ")
	#Enter the values for your equation
	equaY = float(input("Please enter for Y: "))
	equaM = float(input("Please enter for M: "))
	equaB = float(input("Please enter for B: "))
	# shows equation and asks if it is correct
	print(equaY, " = ", equaM, "x", " + ", equaB)
	confirm = input("Is this equation correct? y/n: ")

	if confirm == "y":
		print("Ok! Lets begin to solve this equation.")
		equaY = equaY - equaB
		equaB = 0
		equaY = equaY/equaM
		equaM = 0
		print("And the Answer is ", equaY)
		print("_____________________________________________________")

	else:
		print("I'm sorry, but the equation you entered is invalid!")
		running = False

