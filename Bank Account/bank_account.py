class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self,initialAmount, account_name):
        self.balance=initialAmount
        self.name=account_name
        print(f"\n Account '{self.name}' created.\nBalance= ${self.balance:.2f}")
    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance=${self.balance:.2f}")  
    
    def deposit(self,amount):
        self.balance=self.balance+amount  
        print('\nDeposit Completed')  
        self.getBalance()

    def feasibleTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' has only a balance of ${self.balance:.2f}"
            )
    def withdraw(self,amount):
        try:
            self.feasibleTransaction(amount)
            self.balance=self.balance-amount
            print("\nWithdraw Complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\n Withdraw Interrupted: {error}')
    
    def transfer(self,amount,account_name):
        try:
            print('\n**********\n\n Beginning Transfer..🚀')
            self.feasibleTransaction(amount)
            self.withdraw(amount)
            account_name.deposit(amount)
            print('\nTransfer Complete..✅\n\n*****')
        except BalanceException as error:
            print(f'\nTransfer Interrupted..❌ {error}')


class InterestRewards(BankAccount):
    def deposit(self, amount):
        self.balance=self.balance +(amount * 1.05)
        print('\nDeposit Complete')
        self.getBalance()

class SavingsAcct(InterestRewards):
    def __init__(self, initialAmount, account_name):
        super().__init__(initialAmount, account_name)
        self.fee=4
    def withdraw(self, amount):
        try:
            self.feasibleTransaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("\nWithdraw Completed")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw Interrupted: {error}')