#!/usr/bin/python3
guests = [ 'hitler', 'jimmy Urine', 'god' ]

# The invitations
print(f"Hello {guests[0].title()} You are invited to dinner!")
print(f"Hello {guests[1].title()} You are invited to dinner!")
print(f"Hello {guests[2].title()} You are invited to dinner!")

# Hitler couldn't make it to dinner
print(f"\n{guests[0]} cant make it")
del guests[0]

# Inviting my mom to dinner 
guests.insert(0, 'Mom')

# The New guest invitations
print(f"Hello {guests[0].title()} You are invited to dinner!")
print(f"Hello {guests[1].title()} You are invited to dinner!")
print(f"Hello {guests[2].title()} You are invited to dinner!")

# Informing the guest list
print(f"Hello {guests[0]}, {guests[1]}, and {guests[2]} I have found a bigger table for dinner")
print(len(guests))

# Adding more guests
guests.insert(0, 'alex')
guests.insert(3, 'josh')
guests.append('craig')
print(f"\n\t---------THE NEW INVITATIONS--------")
print(f"Hello {guests[0].title()} You are invited to dinner!")
print(f"Hello {guests[1].title()} You are invited to dinner!")
print(f"Hello {guests[2].title()} You are invited to dinner!")
print(f"Hello {guests[3].title()} You are invited to dinner!")
print(f"Hello {guests[4].title()} You are invited to dinner!")
print(f"Hello {guests[5].title()} You are invited to dinner!")

# removing guests
print(f"I am sorry to inform you: {guests[5]}, {guests[4]}, {guests[3]}, {guests[2]} The table will not be ready in time")
guests.pop(5); guests.pop(4); guests.pop(3); guests.pop(2)

# The final guest list after removing guests
print(f"\n\t-----------GUEST LIST CHANGED------------")
print(f"{guests[0]} you are still invited to dinner")
print(f"{guests[1]} you are still invited to dinner")
print(guests)

# Deleting the final two guests from the list
del guests[0]; del guests[0]

# No more guests remain
print(guests)
