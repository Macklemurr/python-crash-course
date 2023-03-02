#!/usr/bin/python
#7-1 Rental Car
"""
rental_car = input("What kind of rental car would you like? ").title()

print(f"Let me find you a {rental_car}")
"""

#7-2 Restaurant Seating
"""
people = input("How many people will be seated today? ")
people = int(people)

if people > 8:
	print("Sorry, the wait time will longer than expected." 
	"You'll have to wait for a table")
else:
	print("Your table is ready, come right here")
"""

#7-3 Multiples of Ten
"""
number = input(f"Put a number here, \nand ill see if it's a multiple of 10: ")
number = int(number)

if number % 10 == 0:
	print(f"{number} is a multiple of 10")
else:
	print(f"{number} is not")
"""

# 7-4 Pizza Toppings
"""
pizzaToppings = "\nWelcome to Pizza Hut, What would you like on your pizza?"
pizzaToppings += "\n(Enter in 'quit' to exit)\n"

toppingList = []
active = True

while active == True:
	topping = input(pizzaToppings)
	topping = str(topping)

	if topping == 'quit':
		break
	else:
		print(f"\nWe will add {topping} to your pizza :3")
		toppingList.append(topping)
"""

# 7-5 Movie Tickets
"""
age = int(input("To determine the movie ticket price, What is your age?"))

active = True
while True: 
	if age < 3:
		cost = 0
		break

	elif age in range(3, 13):
		cost = 10
		break

	else:
		cost = 15
		break

print(f"Your total for the ticket is ${cost}")
"""

# 7-6 Three Exits
"""
pizzaToppings = "\nWelcome to Pizza Hut, What would you like on your pizza?"
pizzaToppings += "\n(Enter in 'quit' to exit)\n"

toppingList = []
topping = ""

active = True
while active:
	topping = input(pizzaToppings)
	if (topping == 'quit'):
		actve = False
		print("I've placed your order")
		 
	else:
		print(f"\nWe will add {topping} to your pizza :3")
		toppingList.append(topping)
"""
# 7-7 Infinity
"""
import signal
import sys
import time

message = "\n(Press ctrl+c to stop)"
message += "\nPress enter to continue..."

active = True
dataSig = 1 

def int_handler(signum, frame):
	print(f"{dataSig}")
	sys.exit()


def mainFuncs():
	input(message)
	while True:
		dataSig += 1
		print("lol")
		time.sleep(0.3)

if __name__ == '__main__':
	signal.signal(signal.SIGINT, int_handler)

	mainFuncs()
"""

# 7-8 Deli
"""
sandwichOrders = [ 'chicken', 'salami', 'ham', 'turkey' ]

finishedSandwiches = []

while sandwichOrders:
	currentOrder = sandwichOrders.pop()

	finishedSandwiches.append(currentOrder)
	print(f"\nI made your {currentOrder} sandwich")

	if len(sandwichOrders) == 0:
		print('All sandwiches have been made')
	else:
		print(f"We have {len(sandwichOrders)} orders left")
"""

# 7-9 No Pastrami
"""
sandwichOrders = [ 'chicken', 'salami', 'pastrami', 'ham', 'pastrami', 'turkey', 'pastrami' ]

finishedSandwiches = []

print("The deli has ran out of pastrami")

while 'pastrami' in sandwichOrders:
	sandwichOrders.remove('pastrami')

while sandwichOrders:
	currentOrder = sandwichOrders.pop()

	finishedSandwiches.append(currentOrder)
	print(f"\nI made your {currentOrder} sandwich")

	if len(sandwichOrders) == 0:
		print('All sandwiches have been made')
	else:
		print(f"We have {len(sandwichOrders)} orders left")
"""

# 7-10 Dream Vacation
greeter = "\nWe are doing a poll on your dream vacation. "
greeter += "To participate in this poll, please provide us your name \n"

poller = "Whats your name? \n"

poll = "\nIf you visit one place, where would you go? \n"
poll += "(Type 'quit' to exit the program)\n"

pollResults = {}

active = True

while active == True:
	print(greeter)
	name = input(poller)
	vacationLocation = input(poll)
	
	if vacationLocation == 'quit':
		active = False

	pollResults[name] = vacationLocation
	repeat = input("\nWould you like to poll another person? (yes/no)")
	
	if repeat == 'no':
		active = False

for name, location in pollResults.items():
	print(f"\n{name} would love to go to {location}")