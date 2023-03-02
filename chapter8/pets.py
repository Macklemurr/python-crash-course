def describe_pet(pet_name, animal_type='dog'):
    '''Displays information about pets'''
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s namw is {pet_name.title()}")

describe_pet(pet_name='willie')