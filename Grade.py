while True:
    score = int(input("Enter your score (0-100): "))

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

    # Keep asking until the user enters yes or no
    while True:
        choice = input("\nDo you want to calculate another grade? (yes/no): ").strip().lower()

        if choice == "yes":
            break          # Exit this loop and ask for another score
        elif choice == "no":
            exit()         # Ends the program
        else:
            print("Invalid input! Please enter only 'yes' or 'no'.")