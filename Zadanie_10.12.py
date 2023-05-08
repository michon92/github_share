import json

#this program's marging Zadanie_10.11_getnumber.py
# and Zadanie_10.11_loadnumber.py

def get_number():
    """Define your favorite number"""
    while True:
        try:
            favorite_number = int(input("Type your favorite number: \n> "))
        except ValueError:
            print("Wrong input types please input integer next time")
        else:
            filename = 'favorite_number.json'
            with open(filename, 'w') as f:
                json.dump(favorite_number, f)
            return favorite_number


def load_number():
    """Load favorite number if that file exist*"""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            favorite_number = json.load(f)
    except FileNotFoundError:
        print(f"File '{filename}' doesn't exist :( :( :(")
    else:
        return favorite_number


def get_stored_number():
    """Load or define doesn't exist users favorite number"""
    favorite_number = load_number()
    if favorite_number:
        print(f"I know yours favorite numbers.\nIt's '{favorite_number}'.")
    else:
        favorite_number = get_number()
        print(f"Your favorite number '{favorite_number}' was saved xD")


get_stored_number()
