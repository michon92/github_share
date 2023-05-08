import json


def load_number():
    """Load favorite number if that file exist*"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        print(f"File '{filename}' doesn't exist :( :( :(")
    else:
        print(f"I know your favorite number: {favorite_number}")


load_number()