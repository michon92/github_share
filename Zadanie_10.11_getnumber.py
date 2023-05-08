import json


def get_number():
    """Define your favorite number"""
    favorite_number = input("Type your vavorite number: \n> ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(favorite_number, f)
    return favorite_number


get_number()