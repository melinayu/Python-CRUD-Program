def input_valid_age(prompt):
    """Function to get valid values from user input

    Args:
        choice (int): just select a integer 
                    number with a max value of 30

    """
    while True:
        try:
            age = int(input("Enter new employee's age: "))
            if 0 < age <= prompt:
                return age
            else:
                print("Age must be a positive number less than 31. Please try again.")
        except ValueError:
            print("\nInvalid age. Please enter a number!\n")

def input_user_choice(prompt):
    """The user will enter a valid choice from sub menu.

    Args:
        choice (int): just selects a integer number

    """
    while True:
        try:
            input_user = int(input("Please choose sub menu: "))
            if 1 <= input_user <= prompt:
                return input_user
            else:
                print("Invalid Number!. Please enter a valid choice.\n")
        except ValueError:
            print("Invalid! Please enter a valid number.\n")

def input_ask_user(prompt):
    """The user will enter a confirm choice.

    Args:
        ask (str): just selects a string confirmation according to question.

    """
    while True:
        save_the_data = input(f"{prompt}[yes/no] : ").strip().lower()
        if save_the_data == 'yes':
            return True
        elif save_the_data == 'no':
            print("You choose no! so selection cannot be processed.\n")
            break
        else:
            print("Invalid! Please enter 'yes' for continue the next option or 'no' for cancel.\n")