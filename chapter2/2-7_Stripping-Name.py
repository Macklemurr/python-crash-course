#!/usr/bin/python3
first_name = ' Austin '
last_name = ' Bell '
full_name = f"My Name: \t\n{first_name}\n{last_name}"

print("My Name:" f"\t\n{first_name}\n{last_name}".strip())
print("My Name:" f"\t\n{first_name}\n{last_name}".lstrip())
print("My Name:" f"\t\n{first_name}\n{last_name}".rstrip())

print(f"{full_name}".strip())
print(f"{full_name}".lstrip())
print(f"{full_name}".rstrip())
