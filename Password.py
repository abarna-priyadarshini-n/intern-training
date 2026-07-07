stored_password = "Welcome@123"

while True:
    password = input("Enter your password: ")

    if password == stored_password:
        print("Login Successful!")
        break          
    else:
        print("Incorrect Password!")

        while True:
            choice = input("Do you want to try again? (yes/no): ").strip().lower()

            if choice == "yes":
                break     
            elif choice == "no":
                exit()     
            else:
                print("Invalid input! Please enter only 'yes' or 'no'.")