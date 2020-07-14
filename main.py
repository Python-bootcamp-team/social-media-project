def get_valid_input():
    choice = 0
    valid = False
    while not valid:
        try:
            choice = int(input(">> "))
            valid = True
        except ValueError:
            print("Invalid input")
    return choice


def border():
    temp_string = ""
    for i in range(15):
        temp_string += "-"
    print(temp_string)


def login():
    border()
    user = input("\nUser name: ")
    pswd = input("\nPassword: ")


def main():
    pass

main()