# 9-1 Resaurant
"""
class Restaurant:
	
	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine
		
	def describe_restaurant(self):
		print(f"Welcome to {self.name}")
		print(f"We serve {self.cuisine}")
		
	def open_restaurant(self):
		print(f"{self.name} is now open!")
		
		
pizza = Restaurant('peppinos pizza', 'pizza')

pizza.open_restaurant()
pizza.describe_restaurant()
"""

# 9-2 Three Restaurants
"""
class Restaurant:
	
	def __init__(self, name, cuisine):
		self.name = name.title()
		self.cuisine = cuisine
		
	def describe_restaurant(self):
		print(f"Welcome to {self.name}")
		print(f"We serve {self.cuisine}")
		
	def open_restaurant(self):
		print(f"\n{self.name} is now open!")
		
		
pizza = Restaurant('peppinos pizza', 'pizzas')
chipotle = Restaurant('chipotle', 'burritos')
mcdonalds = Restaurant('mcDonalds', 'burgers')

chipotle.open_restaurant()
chipotle.describe_restaurant()

mcdonalds.open_restaurant()
mcdonalds.describe_restaurant()

pizza.open_restaurant()
pizza.describe_restaurant()
"""

# 9-3 Users
"""
class Users:
	
	def __init__(self, first, last, age, gender):
		self.first = first.title()
		self.last = last.title()
		self.age = age
		self.gender = gender
		
	def describe_user(self):
		print(f"{self.first} {self.last} is {self.age} years old, and",
		f"identifies as {self.gender}")
		
	def greet_user(self):
		print(f"\nWelcome {self.first} {self.last}!")

briant_lee = Users('briant', 'lee', 3, 'braint')
ed_knight = Users('ed', 'knight', 19, 'male')
austin_bell = Users('austin', 'bell', 27, 'male')

austin_bell.greet_user()
austin_bell.describe_user()

ed_knight.greet_user()
ed_knight.describe_user()

briant_lee.greet_user()
briant_lee.describe_user()
"""

