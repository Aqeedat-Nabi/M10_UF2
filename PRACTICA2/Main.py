# Import CRUD operations:
from create_table import create_table
from create import create_user
from read import read_user
from update import user_update
from delete import delete_user

# Define the main function including try block and catch exceptions:
def main():
    try:
        # The user is prompted to decide whether to create a new table 
        create_table_option = input("Do you want to create a new table ? (yes / no): ").lower()

        # in case of creating a table
        if create_table_option == "yes": 
            # call the method to create it
            create_table()
            print("Table 'USERS' created successfully.")

        # in other case , A while loop is initiated, presenting a menu 
        # with options for CRUD operations from the user :
        while True:
            print("\n Choose an option :")
            print("1. Create User")
            print("2. Read Users")
            print("3. Update User")
            print("4. Delete User")
            print("5. Exit")

            # asking for user input
            choice = input("Enter your choice between 1 to 5 : ")

            if choice == '1':
                user_id = int(input("Enter user ID : "))
                user_name = input("Enter user_name : ")
                user_surname = input("Enter user_surname : ")
                user_age = int(input("Enter user_age : "))
                user_email = input("Enter user_email : ")
                user_address = input("Enter user_address : ")
                
                # after taking values from the user call the methed to create a new user inside the table USERS
                create_user(user_id, user_name, user_surname, user_age, user_email, user_address)
                print("User Created successfully , with ID : " , user_id)

            elif choice == '2':
                # displaying all the users inside the table
                print("The users are as follows : \n")
                read_user()

            elif choice == '3':
                user_id = int(input("Enter user ID to update : "))
                modification = {
                    'user_name': input("Enter new user_name : "),
                    'user_surname': input("Enter new user_surname : "),
                    'user_age': int(input("Enter new user_age : ")),
                    'user_email': input("Enter new user_email : "),
                    'user_address': input("Enter new user_address : ")
                }
                # asking for thee fields and id to modify and calling the respective method
                # to make updates
                user_update(user_id , modification)
                print("User Updated Successfully.")

            elif choice == '4':
                user_id = int(input("Enter user ID to delete : "))
                # taking the user_id and deleting the user from the table 
                # by calling the respective function 
                delete_user(user_id)
                print("User Deleted successfully.")

            elif choice == '5':
                # leaving the while loop 
                print(" Terminating the program according to your choice !")
                break

            else:
                # Invalid choice , in case ...
                print("Incorrect option , Enter a number between 1 and 5 ONLY ...")

    # handle the exceptions : 
    except Exception as e:
        print(f" There's an ERROR .. :(  {str(e)}")

# Run the main function 
if __name__ == "__main__":
    main()
