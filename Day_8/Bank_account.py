"""Create a Bank Account Framework using OOP 
You can deposit and withdraw from the account
"""

class BankAccount:
    def __init__(self, balance: int) -> None:
        self._balance = balance
    
    @property
    def balance(self) -> int:
        return self._balance
    
    def withdraw(self, amount: int) -> None:
        if amount > self._balance:
            raise ValueError("Insufficient Funds")
        self._balance -= amount
        
    def deposit(self, amount: int) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be a positive amount")
        self._balance += amount
        
def main() -> None:
    account = BankAccount(200)
    account.withdraw(50)
    account.deposit(120)
    print(account.balance)  # using a method like an attribute


if __name__ == "__main__":
    main()