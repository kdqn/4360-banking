import sys

class Auth:
    def __init__(self):
        self.login_attempts = 0

    def login(self):
        if self.login_attempts >= 3:
            print("Sorry you've tried 3 times. Goodbye.")
            sys.exit(1) #Gracefully Exit
            
        username = "kdqn"
        password = "potato"
        print("Enter username:")
        login_username = input()
        print("Enter password:")
        login_password = input()
        if login_username == username and login_password == password:
            print("Yep, you're in!")
            return True
        else:
            print("Nope, wrong username or password")
            self.login_attempts += 1

            return False

class Actions:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient funds")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def get_balance(self):
        print(f"Current balance is {self.balance}.")
        return self.balance

    def transfer(self, amount, account):
        if amount <= self.balance:
            self.balance -= amount
            account.deposit(amount)
            print(f"Transferred {amount} to account. New balance is {self.balance}.")
        else:
            print("Insufficient funds")

    def show_options(self, another_account):
        while True:
            print("\nChoose an action:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Get Balance")
            print("4. Transfer")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '3':
                print("Account 1:")
                self.get_balance()
                print("Account 2:")
                another_account.get_balance()
            elif choice == '4':
                amount = float(input("Enter amount to transfer: "))
                donor_choice = input("Choose donor account (1 for current account, 2 for another account): ")
                if donor_choice == '1':
                    self.transfer(amount, another_account)
                elif donor_choice == '2':
                    another_account.transfer(amount, self)
                else:
                    print("Invalid choice. Please try again.")
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again. hint:(Use ONLY numbers)")
