#!/usr/bin/python
"""
	Chapter 6 - Dictionaries
	Python Crash Course
"""

# 6-1 Person
"""
alex = {
	'firsT_name': 'alex',
	'last_name':  'zavala',
	'age':	'27',
	'city': 'Manassas',
	}
robby = {
	'firt_name': 'robby',
	'last_name': 'whetzel',
	'age':	'28',
	'city': 'arlington',
	}
print(alex)
print(robby)
"""

# 6-2 Favorite Numbers
"""
favorite_numbers = {
	'alex': '666',
	'oscar': '50',
	'josh': '10',
	}
alex_num = favorite_numbers['alex']
oscar_num = favorite_numbers['oscar']
josh_num = favorite_numbers['josh']

print(f"Alex's favorite number is {alex_num}")
print(f"Oscar's favorite number is {oscar_num}")
print(f"Josh's favorite number is {josh_num}")
"""

# 6-3 Glossary
"""
defintions = {
	'else': 'The else keyword catches anything which isnt caught by the preceding conditions.', 
	'list': 'a collection of items in a particular order',
	}
word = 'else'
print(f"\n{word.title()}: {defintions['else']}")

word = 'list'
print(f"\n{word.title()}: {defintions['list']}")
"""

# 6-4 Glossary 2
"""
definitions = {
	'else': 'The else keyword catches anything which isnt caught by the preceding conditions.', 
	'list': 'a collection of items in a particular order',
	'boolean': 'another term for a conditional test',
	'tuple': 'value that can not change',
	}

for keys, values in definitions.items():
	print(f"{keys.title()}: {values.title()}")
"""

# 6-5 Rivers
"""
rivers = {
	'amazon': 'brazil, peru, and columbia',
	'nile': 'egypt',
	'ganges': 'india and bangladesh',
}
for key, value in sorted(rivers.items()):
	print(f"The {key.title()} runs in {value.title()}")

print(f"\nEvery river in the list: ")
for key in set(rivers.keys()):
	print(f"{key.title()}")

print(f"\nEvery Country(ies) in the dictionary: ")
for value in set(rivers.values()):
	print(f"{value.title()}")
"""	

# 6-6 Polling
"""
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
	'person': 'java',
}
people_required = ['kim', 'alex', 'phil']

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print(f"\n")

for needed in people_required:
	if needed in favorite_languages.keys():
		print(f"{needed.title()}, thanks for taking the poll!")
	else:
		print(f"{needed.title()},take the poll")	
"""

# 6-7 People
"""
people = [ ]

person = {
	'first_name': 'alex',
	'last_name':  'zavala',
	'age':	'27',
	'city': 'manassas',
	}
people.append(person)

person = {
	'first_name': 'robby',
	'last_name': 'whetzel',
	'age':	'28',
	'city': 'arlington',
	}
people.append(person)

person = {
	'first_name': 'john',
	'last_name': 'bell',
	'age': '64',
	'city': 'manassas',
}
people.append(person)

for persons in people:
	print(f"{persons['first_name'].title()} {persons['last_name'].title()} is {persons['age']}, living in {persons['city'].title()}")
"""

#6-8 Pets
"""
pet = []
cat = {
	'name': 'kitty',
	'owner': 'austin',
}
pet.append(cat)
dog = {
	'name': 'king',
	'owner': 'ness',
}
pet.append(dog)

for pets in pet:
	name = pets['name'].title()
	owner = pets['owner'].title()
	print(f"{name} is owned by {owner}")
"""

#6-9 Favorite Places
"""
favorite_places = {
	'alex': [ 'czechoslovakia', 'el salvador'],
	'austin': [ 'philadelphia', 'australia' ],
	'robby': ['japan', 'china'],
}

for name, place in favorite_places.items():
	print(f"{name.title()} favorite places are: ")
	for places in place:
		print(f"{places.title()}")
"""

#6-10 Favorite Numbers
"""
favorite_numbers = {
	'alex': [ '666', '123' ],
	'oscar': [ '50', '100' ],
	'josh': [ '10', '40' ],
	}
alex_num = favorite_numbers['alex'] 
oscar_num = favorite_numbers['oscar']
josh_num = favorite_numbers['josh']

for name, numbers in favorite_numbers.items():
	print(f"{name.title()}'s favorite number is: ")
	for fav_number in numbers:
		print(f"{fav_number}")
"""
#6-11 Cities\
"""
cities = {
	'memphis': ['Named for its Egyptian sister on the Nile.', '620,702', 'united states, tennesse'],
	'atlanta': ['atlanta was the only city in North American destroyed as an act of war.', '6,013,000', 'united states, georgia'],
	'burlington': ['the worlds tallest file cabinet is in Burlington, Vermont.', '44,743', 'united states, vermont'],
}
for city, city_facts in cities.items():
	print(f"\n{city.title()}: ")
	for city_facts in city_facts:
		print(f"\t{city_facts.title()}")
"""
#6-12 Extensions
"""
employees = {
    'abell': {
        'first': 'austin',
        'last': 'bell',
        'email': 'austin.bell@ibm.com',
        'numbers': [ '7','8','9' ],
    },
    'avala': {
        'first': 'alex',
        'last': 'zavala',
        'email': 'alex.zavala@ibm.com',
        'numbers': [ '4','5','6' ],
    },
    'juire': {
        'first': 'josh',
        'last': 'mcguire',
        'email': 'josh.mcguire@ibm.com',
        'numbers': [ '1','2','3' ],
    },
}   


for username, info in employees.items():
    numbers = info['numbers']
    full_name = f"{info['first']} {info['last']}"
    email = f"{info['email']}"
    print(f"\nViewing info for: {username}"), input(f"\tPress Any Key to view info ")
    print(f"\nFull name of the user: "), print(full_name)
    print(f"\nTheir work email is : "), print(email)
    for numbers in numbers:
        print(f"\nTheir favorite numbers are: {numbers}")
"""