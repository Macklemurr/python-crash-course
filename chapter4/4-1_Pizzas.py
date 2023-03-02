#!/usr/bin/python3
pizzas = ['meat lovers', 'artichoke', 'pepperoni']
friends_pizza = pizzas[:]

for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("I like many different kinds of pizza")
print("I like pizzas so much that I work at a pizza place")
print("The marinara is my favorite part of pizza")
print("I really love pizza")

pizzas.append('salami')
friends_pizza.append('anchovie')

print(" ")
print("My favorites pizzas are: ")
for my_list in pizzas[:]:
    print(my_list.title())

print(" ")
print("My Friends favorite pizzas are: ")
for friends_list in friends_pizza:
    print(friends_list.title())
