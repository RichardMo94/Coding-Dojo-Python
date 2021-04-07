class BankAccount:
    def __init__(self, int_rate, balance):
        self.interest = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee!")
        self.balance -= amount
        return self
        

    def displayAccount(self):
        print(f'Balance: ${self.balance}')
        return self

    def yieldInterest(self):
        if self.balance < 0:
            print('Balance is negative!')
            return self
        self.balance = (self.balance * self.interest) + self.balance
        return self

account1 = BankAccount(.01, 100)
account2 = BankAccount(.02, 100)

account1.deposit(100).deposit(100).deposit(50).withdraw(50).yieldInterest().displayAccount()

account2.deposit(200).deposit(200).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yieldInterest().displayAccount()