# Give a prompt to the user asking if they wish to create a new savings account or access an existing one
# If the user would like to create a new account, accept their name and initial deposit
# Create a 5 digit number and make it as the account number of their new savings account
# If they are accessing an existing account, accept their name and account number to validate the user
# Give them options to withdraw, deposit or display their available balance

from abc import abstractmethod, ABCMeta
from random import randint

class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0
    @abstractmethod
    def authenticate():
        return 0
    @abstractmethod
    def withdraw():
        return 0
    @abstractmethod
    def deposit():
        return 0
    @abstractmethod
    def displayBalance():
        return 0


class SavingsAccount(Account):
    def __init__(self):
        # [key][0] => name ; [key][1] => balance
        self.savingsAccounts = {}
    def createAccount(self, name, initialDeposit):
        # randint() ==> generate a random number based on a digit you pass
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("Account created succefully. Your account number is ", self.accountNumber)

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber][0] == name:
                print('Athentication is succeful')
                self.accountNumber = accountNumber
                return True
            else:
                print('Athentification failed')
                return False
        else:
            print('Athetification failed!')
            return False

    def withdraw(self, withdrawalAmount):
        if withdrawalAmount > self.savingsAccounts[self.accountNumber][1]:
            print('Insifficient balance')
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawalAmount
            print("Withdrawal was succeful.")
            self.displayBalance()
        

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] =+ depositAmount
        print("Deposit was succeful.")
        self.displayBalance()


    def displayBalance(self):
        print("Available balance: ",self.savingsAccounts[self.accountNumber][1])
        

savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access an existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter your name: ")
        name = input()
        print('Enter the initial deposit: ')
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
        
    elif userChoice is 2:
        print('Enter your name: ')
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input())
        authenticationStatus = savingsAccount.authenticate(name, accountNumber)
        if authenticationStatus is True:
            while True:
                print("Enter 1 to withdraw")
                print("Enter 2 to deposit")
                print("Enter 3 to display available balance")
                print("Enter 4 to go back to the previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    print('Enter withdrawal amount')
                    withdrawalAmount = int(input())
                    savingsAccount.withdraw(withdrawalAmount)
                elif userChoice is 2:
                    print("Enter an amount to be deposited")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
        quit()