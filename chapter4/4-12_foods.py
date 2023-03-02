#!/usr/bin/python3
my_foods = ['pizza', 'falafel', 'carrot cake']
my_friends = my_foods[:]

my_foods.append('cannoli')
my_friends.append('ice cream')

print("My favorite foods are: ")
for favorite_foods in my_foods:
    print(favorite_foods.title())
print(" ")
print("My friends favorite foods are: ")
for friends_favorite in my_friends:
    print(friends_favorite.title())
