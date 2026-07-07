while True:
    number = int(input("Enter a number: "))

    # positive, negative, or zero
    if number > 0:
        print("The number is Positive.")
    elif number < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")

    # even or odd
    if number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")

    # Ask if the user wants to continue
    choice = input("\nDo you want to check another number? (yes/no): ").strip().lower()

    if choice != "yes":
        break