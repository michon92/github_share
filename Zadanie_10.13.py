import json
#example from book

def get_stored_username():
    """Load username if it was saved"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_usernname():
    """Define username by user and save it as JSON file"""
    username = (input("Please, input your name: \n> "))
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Program greets user using his name"""
    username = get_stored_username()
    if username:
        current_name = input(f"Is it you, {username.title()}, "
                             f"choose 'Y' or 'N' ?\n>").upper()
        if current_name != 'Y':
            username = get_new_usernname()
            print(f"Your name was saved and will be load in the future: "
                  f"{username.title()}")
        else:
            print(f"Nice to see you back :), {username.title()}!")
    else:
        username = get_new_usernname()
        print(f"Your name was saved and will be load in the future: "
              f"{username.title()}")


greet_user()