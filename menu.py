import addition
import multiplication
import subtract
import division
print("1: Addition, 2: Subtraction, 3: Multiplication, 4: Division")

inp = input("Enter the choice: ")

if inp == 1:
	addition.add()
elif inp == 3:
	multiplication.multiplication()
elif inp == 2:
	subtract.subtraction()
elif inp == 4:
	division.division()
else:
	print("Invalid input")