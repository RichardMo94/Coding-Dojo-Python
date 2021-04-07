class user:
    def __init__(self, name, email_adress):
        self.name = name
        self.email = email_adress
        self.accountBal = 0
    
    def make_deposit(self, amount):
        self.accountBal += amount
        return self

    def make_withdraw(self, amount):
        self.accountBal -= amount
        return self

    def make_transfer(self, otherUser, amount):
        self.accountBal -= amount
        otherUser.accountBal += amount
        return self
        
    def displayBalance(self):
        print(f"User: {self.name}, Balance: ${self.accountBal}")
        return self


richard = user('Richard Morales', 'richy@dojo.com')
chris = user('Chris Medlin', 'chris@yahoo.com')
jon = user('Jon Huerta', 'jon@gmail.com')

richard.make_deposit(100).make_deposit(100).make_deposit(100).make_withdraw(100).displayBalance()

chris.make_deposit(100).make_deposit(100).make_withdraw(50).make_withdraw(50).displayBalance()

jon.make_deposit(300).make_withdraw(50).make_withdraw(50).make_withdraw(50).displayBalance()

richard.make_transfer(jon, 50) 
jon.displayBalance()
richard.displayBalance()