
import random
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        account_number = str(random.randint(100000, 999999))

        self.accounts[account_number] = BankAccount(account_number, 100)

    def display_accounts_and_balances(self):
        for account_number, account in self.accounts.items():
            print(f"Account Number: {account_number}, Balance: {account.display_balance()}")

    def transfer_money(self, amount, from_account, to_account):
        if from_account not in self.accounts or to_account not in self.accounts:
            return "Account does not exist"
        if self.accounts[from_account].balance < amount:
            return "Insufficient funds"
        self.accounts[from_account].withdraw(amount)
        self.accounts[to_account].deposit(amount)
        return self.accounts[from_account].balance

account_manager = AccountManager()
while True:
    print("1. Create account")
    print("2. Display accounts and balances")
    print("3. Transfer money")
    print("4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        account_manager.create_account()
    elif choice == "2":
        print(account_manager.display_accounts_and_balances())
    elif choice == "3":
        from_account = input("Enter from account: ")
        to_account = input("Enter to account: ")
        amount = float(input("Enter amount: "))
        print(account_manager.transfer_money(amount, from_account, to_account))
    elif choice == "4":
        break
    else:
        print("Invalid choice")