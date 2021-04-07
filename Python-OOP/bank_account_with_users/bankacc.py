class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest = int_rate
        self.balance = balance

class user:
    def __init__(self, name, email_adress):
        self.name = name
        self.email = email_adress
        self.account = BankAccount(int_rate=.02, balance=100)

    def deposit(self, amount):
        self.account.balance += amount
        return self

    def withdraw(self, amount):
        if self.account.balance < amount:
            print("Insufficient funds: Charging a $5 fee!")
        self.account.balance -= amount
        return self
        

    def displayAccount(self):
        print(f'Balance: ${self.account.balance}')
        return self

    def yieldInterest(self):
        if self.account.balance < 0:
            print('Balance is negative!')
            return self
        self.account.balance = (self.account.balance * self.account.interest) + self.account.balance
        return self

richard = user('Richard Morales', 'richy@dojo.com')
chris = user('Chris Medlin', 'chris@yahoo.com')
jon = user('Jon Huerta', 'jon@gmail.com')