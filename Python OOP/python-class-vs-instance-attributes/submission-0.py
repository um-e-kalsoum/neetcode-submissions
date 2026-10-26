class BankAccount: 
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name, balance) -> None:
        self.__name = name
        self.__balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    
    @property
    def name(self):
        return self.__name
    
    @property
    def balance(self):
        return self.__balance
    
    @name.setter
    def name(self, name):
        self.__name = name

    @balance.setter
    def balance(self, balance):
        self.__balance = balance


# TODO: Create two accounts
a1 = BankAccount("Alice", 1000)
a2 = BankAccount("Bob", 2000)
# TODO: Print the information using the mentioned format
print(f"Alice's balance: ${a1.balance}")
print(f"Bob's balance: ${a2.balance}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")
