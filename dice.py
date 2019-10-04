# Name: Verne Bauman	
# Period 4
# Dice Rolling Simulator
import random
result = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0

amountofdice = int(input("How many dice would you like to be rolled? "))
x = 1
while x <= amountofdice:
	result = random.randint(1, 6)
	print("Congrats you rolled a : " + str(result))
	x = x + 1
	if result == "1":
		one = one + 1
		print(str(one))
	if result == "2":
		two = two + 2
		print("You rolled a 2 + " (str(two)) + "times!")
	if result == 3:
		three = three + 3
		print("You rolled a 3 + " str(three) + "times!")
	if result == "4":
		four = four + 4
		print(str(four))
	if result == "5":
		five = five + 5
		print (str(five))
	if result == "6":
		six = six + 6
		print (str(six))


