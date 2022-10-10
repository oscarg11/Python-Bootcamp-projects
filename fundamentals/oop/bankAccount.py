class BankAccount:

    all_accounts = []

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    #This method increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self
    #prints all instances of a Bank accounts info
    @classmethod
    def get_bank_account_info(cls):
        for account in cls.all_accounts:
            print(account.display_account_info())
        return cls
        
    #decreases the account balance by the given amount 
    #if there are sufficient funds; if there is not enough money, 
    #print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print(f"-{amount}")
        else:
            print("Insuficient funds: Charging a $5 fee")
            self.balance -= 5
        return self   
    #This methods displays the account balance
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    #increases the account balance by the current balance * the interest rate 
    # (as long as the balance is positive)
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self

#USER class: this class uses an Instance of the BankAccount class
#by the name of self.account that uses methods that mirror the 
#methods used in BankAccount. These methods call on those classes.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    
    
#bankAccount instances
account1 = BankAccount(0.03, 1000)
account2 = BankAccount(0.05, 1000)

account1.deposit(100).deposit(45).deposit(100).withdraw(500).yield_interest().display_account_info()
print("----------------------")
account2.deposit(600).deposit(600).withdraw(100).withdraw(80).withdraw(400).withdraw(200).yield_interest().display_account_info()

#call class method
print("----------------------")
BankAccount.get_bank_account_info()

#user class instance
user1 = User(
    name = "oscar g",
    email = "oscar.g2511@gmail.com"
)
print("User class methods:")
user1.make_deposit(100).make_deposit(200).make_withdraw(50).display_user_balance()
