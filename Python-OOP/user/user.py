class user:
    def __init__(self, name, email_adress):
        self.name = name
        self.email = email_adress
        self.accountBal = 0
    
    def make_deposit(self, amount):
        self.accountBal += amount

    def make_withdraw(self, amount):
        self.accountBal -= amount

    def make_transfer(self, otherUser, amount):
        self.accountBal -= amount
        otherUser.accountBal += amount
        
    def displayBalance(self):
        print(f"User: {self.name}, Balance: ${self.accountBal}")


richard = user('Richard Morales', 'richy@dojo.com')
chris = user('Chris Medlin', 'chris@yahoo.com')
jon = user('Jon Huerta', 'jon@gmail.com')

richard.make_deposit(100)
richard.make_deposit(100)
richard.make_deposit(100)
richard.make_withdraw(100)
richard.displayBalance()

chris.make_deposit(100)
chris.make_deposit(100)
chris.make_withdraw(50)
chris.make_withdraw(50)
chris.displayBalance()

jon.make_deposit(300)
jon.make_withdraw(50)
jon.make_withdraw(50)
jon.make_withdraw(50)
jon.displayBalance()

richard.make_transfer(jon, 50)
jon.displayBalance()
richard.displayBalance()