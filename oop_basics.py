# Student Class
class Student:

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying in Grade {self.grade}.")


# Bank Account Class
class BankAccount:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"\n₹{amount} deposited successfully.")
        print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"\n₹{amount} withdrawn successfully.")
            print(f"Current Balance: ₹{self.balance}")
        else:
            print("\nInsufficient Balance!")
            print(f"Current Balance: ₹{self.balance}")

    def show_balance(self):
        print(f"\nCurrent Balance: ₹{self.balance}")


# ==========================
# Number of Students/Accounts
# ==========================

while True:

    number = int(input("Enter the number of Students: "))

    if number >= 2:
        break
    else:
        print("Please enter at least 2.")


# ==========================
# Student Details
# ==========================

students = []

print("\n========== ENTER STUDENT DETAILS ==========")

for i in range(number):

    print(f"\nStudent {i + 1}")

    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")

    student = Student(name, grade)
    students.append(student)

print("\n========== STUDENT ACTIVITIES ==========")

for student in students:
    student.study()


# ==========================
# Bank Account Details
# ==========================

accounts = []

print("\n========== CREATE BANK ACCOUNTS ==========")

for i in range(number):

    print(f"\nBank Account for {students[i].name}")

    balance = float(input("Enter Starting Balance: ₹"))

    account = BankAccount(students[i].name, balance)
    accounts.append(account)


# ==========================
# Bank Account Menu
# ==========================

while True:

    print("\n========== BANK ACCOUNTS ==========")

    for i in range(number):
        print(f"{i + 1}. {accounts[i].account_holder}")

    print(f"{number + 1}. Exit")

    account_choice = int(input("\nSelect an account: "))

    if account_choice == number + 1:
        break

    elif 1 <= account_choice <= number:

        account = accounts[account_choice - 1]

        while True:

            print(f"\n===== {account.account_holder}'s Account =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Back to Account List")

            choice = input("Enter your choice: ")

            if choice == "1":

                amount = float(input("Enter amount to deposit: ₹"))
                account.deposit(amount)

            elif choice == "2":

                amount = float(input("Enter amount to withdraw: ₹"))
                account.withdraw(amount)

            elif choice == "3":

                account.show_balance()

            elif choice == "4":
                break

            else:
                print("Invalid choice!")

    else:
        print("Invalid account selection!")


# ==========================
# Final Balances
# ==========================

print("\n========== FINAL ACCOUNT BALANCES ==========")

for account in accounts:
    print(f"{account.account_holder} : ₹{account.balance}")

print("\nProgram Completed Successfully!")