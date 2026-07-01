while True:
    print("\n===== LOOPS EXERCISES =====")
    print("1. Multiplication Table")
    print("2. Sum of Numbers (1-100)")
    print("3. FizzBuzz (1-50)")
    print("4. Number Guessing Game")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    # ------------------------------
    # 1. Multiplication Table
    # ------------------------------
    if choice == "1":

        while True:
            number = int(input("Enter a number: "))

            print(f"\nMultiplication Table of {number}")

            for i in range(1, 11):
                print(f"{number} x {i} = {number * i}")

            while True:
                answer = input("\nDo you want another multiplication table? (yes/no): ").strip().lower()

                if answer == "yes":
                    break
                elif answer == "no":
                    break
                else:
                    print("Invalid input! Please enter only 'yes' or 'no'.")

            if answer == "no":
                break

    # ------------------------------
    # 2. Sum of Numbers
    # ------------------------------
    elif choice == "2":

        total = 0

        for i in range(1, 101):
            total += i

        print("\nThe sum of numbers from 1 to 100 is:", total)

    # ------------------------------
    # 3. FizzBuzz
    # ------------------------------
    elif choice == "3":

        for i in range(1, 51):

            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")

            elif i % 3 == 0:
                print("Fizz")

            elif i % 5 == 0:
                print("Buzz")

            else:
                print(i)

    # ------------------------------
    # 4. Number Guessing Game
    # ------------------------------
    elif choice == "4":

        target = 15

        while True:

            guess = int(input("Guess the number: "))

            if guess == target:
                print("Congratulations! You guessed the correct number.")
                break

            elif guess < target:
                print("Too low! Try again.")

            else:
                print("Too high! Try again.")

    # ------------------------------
    # 5. Exit
    # ------------------------------
    elif choice == "5":
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 5.")