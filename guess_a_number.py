
no_win = True
print("I am thinking of a number between 1 and 10.")
while no_win:
    user_number = int(input("What's the number? "))
    try:
        if user_number > 5:
            print(user_number, " is too high.")
        elif user_number == 5:
            print("Yes! You win!")
            no_win = False
        else:
            print(user_number, " is too high.")
    except ValueError:
        print("Please enter a number!")