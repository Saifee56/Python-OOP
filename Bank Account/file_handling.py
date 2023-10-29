from bank_account import *

Saifee= BankAccount(5000,'Saifee')
Safuan= BankAccount(10000,'Safuan')
Saifee.getBalance()
Safuan.getBalance()

Saifee.deposit(3000)

Saifee.withdraw(10000)
Safuan.withdraw(500)

Safuan.transfer(50000,Saifee)
Safuan.transfer(500,Saifee)

Farhan=InterestRewards(1000,'Farhan')
Farhan.getBalance()
Farhan.deposit(100)
Farhan.transfer(100,Saifee)

Rafid=SavingsAcct(1000,'Rafid')
Rafid.getBalance()
Rafid.deposit(100)
Rafid.transfer(10000,Farhan)