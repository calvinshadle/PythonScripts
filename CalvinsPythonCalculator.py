# This is my first program in Python, a Calculator!

print(" ")
print("Calvin's Python Calculator")
print("Made on: 06/01/18")
print(" ")

running = True

while running:
	print("1 = Add")
	print("2 = Subtract")
	print("3 = Multiply")
	print("4 = Divide")
	print("5 = Exit!")
	operation = int(input("Please enter the number according to which operation you would like to perform: "))
	if operation == 1:
		num1 = int(input("Please enter a first number: "))
		num2 = int(input("Please enter a second number: "))
		result = num1 + num2
		print(" ")
		print(num1, " + ", num2, " = ", result)
		print(" ")
	elif operation == 2:
		num1 = int(input("Please enter a first number: "))
		num2 = int(input("Please enter a second number: "))
		result = num1 - num2
		print(" ")
		print(num1, " - ", num2, " = ", result)
		print(" ")
	elif operation == 3:
		num1 = int(input("Please enter a first number: "))
		num2 = int(input("Please enter a second number: "))
		result = num1 * num2
		print(" ")
		print(num1, " * ", num2, " = ", result)
		print(" ")
	elif operation == 4:
		num1 = int(input("Please enter a first number: "))
		num2 = int(input("Please enter a second number: "))
		result = num1/num2
		print(" ")
		print(num1, " / ", num2, " = ", result)
		print(" ")
	elif operation == 5:
		print(" ")
		print("Ok, nevermind then!")
		print(" ")
		running = False