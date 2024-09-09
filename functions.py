class Auth:
    def login(self):
        username = "jcox"
        password = "potato"
        print("Enter username:")
        loginu = input()
        print("Enter password:")
        loginp = input()
        if loginu == username and loginp == password:
            print("Yep, you're in!")
            return True
        else:
            print("Nope, wrong username or password")
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
            print(f"Transferred {amount} to other account. New balance is {self.balance}.")
        else:
            print("Insufficient funds")
    def show_options(account, another_account):
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
                account.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            elif choice == '3':
                account.get_balance()
            elif choice == '4':
                amount = float(input("Enter amount to transfer: "))
                account.transfer(amount, another_account)
            elif choice == '5':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
            