# 1. Number Classifier
def number_classifier():

    while True:
        number = int(input("\nEnter a number: "))

        if number > 0:
            print("The number is Positive.")
        elif number < 0:
            print("The number is Negative.")
        else:
            print("The number is Zero.")

        if number % 2 == 0:
            print("The number is Even.")
        else:
            print("The number is Odd.")

        while True:
            continue_choice = input("\nDo you want to check another number? (yes/no): ").strip().lower()

            if continue_choice == "yes":
                break
            elif continue_choice == "no":
                return
            else:
                print("Invalid input! Please enter only 'yes' or 'no'.")


# 2. Grade Calculator
def grade_calculator():

    while True:
        score = int(input("\nEnter your score (0-100): "))

        if score < 0 or score > 100:
            print("Invalid score! Please enter a score between 0 and 100.")
        elif score >= 85:
            print("Grade: A")
        elif score >= 75:
            print("Grade: B")
        elif score >= 65:
            print("Grade: C")
        elif score >= 55:
            print("Grade: D")
        else:
            print("Grade: F (Fail)")

        while True:
            continue_choice = input("\nDo you want to calculate another grade? (yes/no): ").strip().lower()

            if continue_choice == "yes":
                break
            elif continue_choice == "no":
                return
            else:
                print("Invalid input! Please enter only 'yes' or 'no'.")

# 3. Login Check
def login_check():

    stored_password = "Welcome@123"

    while True:
        password = input("\nEnter your password: ")

        if password == stored_password:
            print("Login Successful!")
            return
        else:
            print("Incorrect Password!")

            while True:
                continue_choice = input("Do you want to try again? (yes/no): ").strip().lower()

                if continue_choice == "yes":
                    break
                elif continue_choice == "no":
                    return
                else:
                    print("Invalid input! Please enter only 'yes' or 'no'.")

# 4. Largest of Three Numbers
def largest_number():

    while True:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))

        if num1 == num2 == num3:
            print("All three numbers are the same.", end=" ")

            if num1.is_integer():
                print(int(num1))
            else:
                print(num1)

        elif num1 >= num2 and num1 >= num3:
            if num1.is_integer():
                print("The largest number is:", int(num1))
            else:
                print("The largest number is:", num1)

        elif num2 >= num1 and num2 >= num3:
            if num2.is_integer():
                print("The largest number is:", int(num2))
            else:
                print("The largest number is:", num2)

        else:
            if num3.is_integer():
                print("The largest number is:", int(num3))
            else:
                print("The largest number is:", num3)

        while True:
            continue_choice = input("\nDo you want to find the largest number again? (yes/no): ").strip().lower()

            if continue_choice == "yes":
                break
            elif continue_choice == "no":
                return
            else:
                print("Invalid input! Please enter only 'yes' or 'no'.")

# MAIN MENU
while True:

    print("\n==============================")
    print(" CONDITIONAL LOGIC EXERCISES ")
    print("==============================")
    print("1. Number Classifier")
    print("2. Grade Calculator")
    print("3. Login Check")
    print("4. Largest of Three Numbers")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        number_classifier()

    elif choice == "2":
        grade_calculator()

    elif choice == "3":
        login_check()

    elif choice == "4":
        largest_number()

    elif choice == "5":
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")