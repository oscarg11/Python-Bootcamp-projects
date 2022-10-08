class BankAccount:

    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
    #This method increases the account balance by the given amount
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    #decreases the account balance by the given amount 
    #if there are sufficient funds; if there is not enough money, 
    #print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
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


account1 = BankAccount(0.03, 1000)
account2 = BankAccount(0.05, 1000)


account1.deposit(100).deposit(45).deposit(100).withdraw(500).yield_interest().display_account_info()
print("----------------------")
account2.deposit(600).deposit(600).withdraw(100).withdraw(80).withdraw(400).withdraw(200).yield_interest().display_account_info()