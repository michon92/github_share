def num_counter():
    """Count two typed numbers, find wrong typos"""
    while True:
        print("Do You want to count some numbers? XD")
        decision = input("If yes, please type 'Y':\n>").upper()
        if decision != 'Y':
            break
        try:
            number_1 = int(input("Type first number:\n>"))
            number_2 = int(input("Type second number:\n>"))
        except ValueError:
            print("Wrong input types please input integer next time")
        else:
            num_count = number_1 + number_2
            print("Count value: " + str(num_count) + ".")
    print("Goodbye!")
num_counter()