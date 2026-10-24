class Account:
    def __init__(self, title, balance):
        self.title = title        # public
        self._balance = balance   # protected
    
    def display_balance(self) -> None:
        print(f"Balance: ${self._balance}")


# Do not modify the code below this line
account = Account("John", 1000)
account.display_balance()
