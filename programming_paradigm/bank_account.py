# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initializes the bank account with an optional starting balance."""
        self._account_balance = initial_balance

    def deposit(self, amount):
        """Deposits the given amount to the account."""
        if amount > 0:
            self._account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws the given amount if sufficient balance is available."""
        if amount > self._account_balance:
            return False  # Insufficient funds
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        else:
            self._account_balance -= amount
            return True

    def display_balance(self):
        """Displays the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")


