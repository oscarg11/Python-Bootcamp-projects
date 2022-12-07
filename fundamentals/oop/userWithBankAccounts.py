#User Class
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)
        
    #methods that call on BankAccounts instance methods
    def make_deposit(self, amount):
        self.account.deposit(amount)

        print(f"New Balance: ${self.account.balance}")
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(f"New Balance: ${self.account.balance}")
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

#Bank Account class
class BankAccount:
    #store BankAccount instances(accounts) in list
    all_accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        
    #deposit function
    def deposit(self,amount):
        self.balance += amount
        return self
    #withdraw
    def withdraw(self,amount):
        self.balance -= amount
        return self
    #display info
    def display_account_info(self):
        print("Your Balance is:",self.balance,"Your interest rate is:",self.int_rate, sep='\n')
        return self
    #interest rate calculation
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self
    
    #NINJA BONUS: Use a classmethod to print all instances of a Bank Account's info
    @classmethod
    def get_all_accounts(cls):
        for account in cls.all_accounts:
            print(f"Balance:${account.balance}, Interest Rate:{account.int_rate}")



# #BankAccount Instances
# account1 = BankAccount(0.01, 0)
# account2 = BankAccount(0.01,0)

# #Make 3 deposits and 1 withdrawl, then yield interest and display the accounts info in one line of code
# print("ACCOUNT 1:")
# account1.deposit(100).deposit(100).deposit(100).withdraw(150).yield_interest().display_account_info()

# #Make 2 deposits and 4 withdrawls,then yield interest and display the accounts info in one line of code
# print("ACCOUNT 2:")
# account2.deposit(1000).deposit(1000).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_interest().display_account_info()

# #prints each instance of BankAccounts stored info
# print("ALL ACCOUNTS IN BankAccount:")
# BankAccount.get_all_accounts()

user1 = User("Oscar","oscar.g2511@gmail.com")

user1.make_deposit(100).make_withdraw(50).display_user_balance()


