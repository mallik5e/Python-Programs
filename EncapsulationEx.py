class BankAccount:
    def __init__(self,account_number,balance=0):
        self._account_number = account_number
        self.__balance = balance 
    
    def get_balance(self):
        return self.__balance 
    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount 
    
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            
bank = BankAccount(21234,1000)
bank.deposit(3000)
print(bank.get_balance())
bank.withdraw(1500)
print(bank.get_balance())