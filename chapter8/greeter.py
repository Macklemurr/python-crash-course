#!/usr/bin/python
import sys

if len(sys.argv) == 3: 
    def greet_user(username, last_name):
        print(f"Hello, {username.title()} {last_name.title()}!")
    greet_user(sys.argv[1], sys.argv[2])
elif len(sys.argv) == 2:
    def greet_user(username):
        print(f'Hello, {username.title()}!')
    greet_user(sys.argv[1])
else:
    print('incorrect usage')
