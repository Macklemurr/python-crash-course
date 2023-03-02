prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished)\n"

while True: # runs until it reaches a break statement
    city = input(prompt)

    if city == 'quit':
        break # end of the while loop
    else:
        print(f"I'd have to go to {city.title()}")
