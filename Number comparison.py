while True:
    num1 = float(input("Enter the first number: "))
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
        choice = input("\nDo you want to find the largest number again? (yes/no): ").strip().lower()

        if choice == "yes":
            break
        elif choice == "no":
            exit()
        else:
            print("Invalid input! Please enter only 'yes' or 'no'.")