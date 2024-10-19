# ===================================
# [New Employees Data in the Company]
# ===================================
# Developed by. [Melin Ayu Safitri]
# JCDS - [Batch 0412]
# /==================================/

from utils.validation_function import input_valid_age, input_user_choice, input_ask_user

new_employees_data = [
    {
        "NIK":  "1234567890",                                                                       
        "name": "Bruno",
        "age": 22,
        "gender":  "Male",
        "domicile":  "Jakarta",
        "position": "Software Engineer",
    },
    {
        "NIK":  "1111111111",
        "name": "Rafael",
        "age": 28,
        "gender":  "Male",
        "domicile":  "Surabaya",
        "position": "Data Scientist",
    },
    {
        "NIK":  "2222222222",
        "name": "Lila Vania",
        "age": 24,
        "gender":  "Female",
        "domicile":  "Malang",
        "position": "Software Engineer",
    },
    {
        "NIK":  "3333333333",
        "name": "Rohan Rizky",
        "age": 24,
        "gender":  "Male",
        "domicile":  "Bogor",
        "position": "UX/UI Designer",
    },
    {
        "NIK":  "4444444444",
        "name": "Aisha Maria",
        "age": 25,
        "gender":  "Female",
        "domicile":  "Depok",
        "position": "Data Scientist",
    },
    {
        "NIK":  "5555555555",
        "name": "Kaito Reihan",
        "age": 28,
        "gender":  "Male",
        "domicile":  "Tangerang",
        "position": "DevOps Engineer",
    },
    {
        "NIK":  "6666666666",
        "name": "Ferro Adrian",
        "age": 30,
        "gender":  "Male",
        "domicile":  "Jakarta",
        "position": "Full Stack Developer",
    },
    {
        "NIK":  "7777777777",
        "name": "Eitan Subhon",
        "age": 22,
        "gender":  "Male",
        "domicile":  "Bandung",
        "position": "Data Analyst",
    },
    {
        "NIK":  "8888888888",
        "name": "Lutfiah Anum",
        "age": 26,
        "gender":  "Female",
        "domicile":  "Surabaya",
        "position": "Cloud Engineer",
    },
    {
        "NIK":  "9999999999",
        "name": "Luna Basri",
        "age": 25,
        "gender":  "Female",
        "domicile":  "Bandung",
        "position": "Software Engineer",
    }
]

def report(new_employees_data):
    """Displays a menu to view information on the list of new employees
    in the company

    This function generate several sub menu with options:
    - Report All Data New Employees
    - Report Certain Data New Employees

    The user's choice determines the subsequent action.
    """
    while True:
        print("\n=====Report Data New Employees the Company=====\n")
        print("1. Report All Data New Employees")
        print("2. Report Certain Data New Employees")
        print("3. Return to main menu\n")
        choice = input_user_choice(3)
        # Displays all new employees data
        if choice == 1:
            print("\n=============================================List New Employees Data=============================================\n")
            print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
            print("| NIK        | Name                      | Age | Gender               | Domicile             | Position             |")
            print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
            for i in new_employees_data:
                print(f"| {i['NIK']:<10} | {i['name']:<25} | {i['age']:<3} | {i['gender']:<20} | {i['domicile']:<20} | {i['position']:<20} |")
            print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+\n")
        # Displays data based on User Input Primary-key
        elif choice == 2:
            # Displays data the user is looking for
            input_data = input("Enter employee NIK: ")
            for i in new_employees_data:
                if i['NIK'] == input_data:
                    print("\n========================================The employee with this NIK : ============================================\n")
                    print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                    print("| NIK        | Name                      | Age | Gender               | Domicile             | Position             |")
                    print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                    print(f"| {i['NIK']:<10} | {i['name']:<25} | {i['age']:<3} | {i['gender']:<20} | {i['domicile']:<20} | {i['position']:<20} |")
                    print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+\n")
                    break
            # If there is no data that the user is looking for
            else:
                print("\nNIK not found in the database")
                break
        # Back to main menu
        elif choice == 3:
            ask = input('Are you sure to return to the main menu? yes/no : ')
            if ask == "yes":
                main()
            elif ask == "no":
                report(new_employees_data)
            else:
                print("\nInvalid! Please enter 'yes' for continue the next option or 'no' for back sub menu")
                break
        # Break while (Back to sub menu report data)
        else:
            break
    report(new_employees_data)

def add(new_employees_data):
    """Displays a menu for adding information of 
    new employees in the company

    This function display a sub menu Add Data New Employee

    The user's choice determines the subsequent action.
    """
    while True:
        print("\n=====Add New Employee Data=====\n")
        print("1. Add Data New Employee")
        print("2. Return to main menu\n")
        choice = input_user_choice(2)

        if choice == 1:
            # Get user input NIK as key to search data
            for i in new_employees_data:
                NIK = input("\nEnter new employee's NIK: ")
                if NIK == i["NIK"]:
                    print("\nNIK already exists in the database!")
                else:
                    name = input("\nEnter new employee's name: ")
                    age = input_valid_age(30)
                    gender = input("Enter new employee's gender: ")
                    domicile = input("Enter new employee's domicile: ")
                    position = input("Enter new employee's position: ")
                    break
            confirm =  input_ask_user('\nAre you sure to save the data?')
            if confirm:
                # Adding new data using append method
                new_employees_data.append({'NIK': NIK, 'name': name, 'age': age, 'gender': gender, 'domicile': domicile, 'position': position})
                print("\nData New Employee Added Successfully")
                # Displays all data after adding new employee data
                print("\n=============================================List New Employees Data=============================================\n")
                print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                print("| NIK        | Name                      | Age | Gender               | Domicile             | Position             |")
                print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                for i in new_employees_data:
                    print(f"| {i['NIK']:<10} | {i['name']:<25} | {i['age']:<3} | {i['gender']:<20} | {i['domicile']:<20} | {i['position']:<20} |")
                print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+\n")
            elif confirm == "no":
                add(new_employees_data) # Back to sub menu add data new employee
        # Back to main menu
        elif choice == 2:
            ask = input('Are you sure to return to the main menu? yes/no : ')
            if ask == "yes":
                main()
            elif ask == "no":
                add(new_employees_data)
            else:
                print("\nInvalid! Please enter 'yes' for continue the next option or 'no' for back sub menu")
                break
    add(new_employees_data)

def update(new_employees_data):
    """Displays a menu to updating information on the list 
    of new employees in the company

    This function display a sub menu Update Data Existing Employee

    The user's choice determines the subsequent action.
    """
    while True:
        print("\n=====Update Existing Employee Data=====\n")
        print("1. Update Data Existing Employee")
        print("2. Return to main menu\n")
        choice = input_user_choice(2)

        if choice == 1:
            # Get user input NIK as key to search data
            NIK = input("Enter NIK to update data: ")
            for i in new_employees_data:
                data_update = None
                if i["NIK"] == NIK:
                    print("\nDisplay data according to the primary key\n")
                    data_update = i
                    if data_update:
                        # Display data to be updated
                        print("==============================================Employee with that NIK:===============================================\n")
                        print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                        print("| NIK        | Name                      | Age | Gender               | Domicile             | Position             |")
                        print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                        print(f"| {i['NIK']:<10} | {i['name']:<25} | {i['age']:<3} | {i['gender']:<20} | {i['domicile']:<20} | {i['position']:<20} |")
                        print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+\n")
                    # Ask user to confirm update data
                    confirm = input_ask_user("Are you sure to update the data?")
                    if confirm:
                        column= input("\nEnter poin in the column: ")
                        if column in data_update:
                            new_value = input(f"Enter new value for {column}: ")
                            # Update data on proccess
                            data_update[column] = new_value
                            print("\nData updated successfully!")
                            # Displays all data after updating
                            print("\n=============================================List Update New Employees Data=============================================\n")
                            print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                            print("| NIK        | Name                      | Age | Gender               | Domicile             | Position             |")
                            print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                            for i in new_employees_data:
                                print(f"| {i['NIK']:<10} | {i['name']:<25} | {i['age']:<3} | {i['gender']:<20} | {i['domicile']:<20} | {i['position']:<20} |")
                            print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+\n")
                            break
                    # If user choose not to update data
                    else:
                        print("\nData has not been updated!")
            # If user input NIK not found in the list
            else:
                print("\nNIK not found in the database!")
        # Back to main menu
        elif choice == 2:
            ask = input('Are you sure to return to the main menu? yes/no : ')
            if ask == "yes":
                main()
            elif ask == "no":
                update(new_employees_data)
            else:
                print("\nInvalid! Please enter 'yes' for continue the next option or 'no' for back sub menu")
                break
        else:
            break
    update(new_employees_data)

def delete(new_employees_data):
    """Displays a menu to deleting information on the list 
    of new employees in the company

    This function display a sub menu Delete Data Existing Employee

    The user's choice determines the subsequent action.
    """
    while True:
        print("\n=====Delete Existing Employee Data=====\n")
        print("1. Delete Data Existing Employee")
        print("2. Return to main menu\n")
        
        choice = input_user_choice(2)

        if choice == 1:
            # Get user input NIK as key to search data
            NIK = input("Enter NIK to delete data: ")
            for i in new_employees_data:
                if i["NIK"] == NIK:
                    # Deleted data from list using remove method
                    new_employees_data.remove(i)
                    print("\nDisplay data according to the primary key\n")
                    # Ask user to confirm delete data
                    confirm = input_ask_user("Are you sure to delete the data?")
                    print("\nData Deleted Successfully")
                    # Display all data after deleting
                    print("\n=============================================List After Delete New Employees Data=============================================\n")
                    print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                    print("| NIK        | Name                      | Age | Gender               | Domicile             | Position             |")
                    print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+")
                    for i in new_employees_data:
                        print(f"| {i['NIK']:<10} | {i['name']:<25} | {i['age']:<3} | {i['gender']:<20} | {i['domicile']:<20} | {i['position']:<20} |")
                    print("+------------+---------------------------+-----+----------------------+----------------------+----------------------+\n")
                    break
            # If user input NIK not found in the list            
            else:
                print("\nData not found in the database!")
                break
        # Back to main menu         
        elif choice == 2:
            ask = input('Are you sure to return to the main menu? yes/no : ')
            if ask == "yes":
                main()
            elif ask == "no":
                delete(new_employees_data)
            else:
                print("\nInvalid! Please enter 'yes' for continue the next option or 'no' for back sub menu")
                break
        else:
            break

    delete(new_employees_data)

# /===== Main Program =====/
def main():
    """Displays the main menu for new employees data in the company.

    This function generate several menu with options:
    - Report Data New Employees
    - Ada Data New Employee
    - Update Data New Employee
    - Delete Data New Employee
    - Exit
    """
    while True:
        print("\n=====Main Menu Program=====\n")
        print("1. Report Data New Employees")
        print("2. Add Data New Employee")
        print("3. Update Data New Employee")
        print("4. Delete Data New Employee")
        print("5. Exit\n")
        input_user = input("Insert your option: ")
        if input_user == "1":
            report(new_employees_data)
        elif input_user == "2":
            add(new_employees_data)
        elif input_user == "3":
            update(new_employees_data)
        elif input_user == "4":
            delete(new_employees_data)
        elif input_user == "5":
            print("\nThe program has ended! Thankyou:)\n")
            exit()
        else:
            print("Input is not valid !")

if __name__ == "__main__":
    main()