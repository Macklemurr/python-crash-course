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