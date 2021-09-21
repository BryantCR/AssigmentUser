class User:

    allUsersAccount = []

    def __init__(self, accountNum = "00000", owner = "N/A" ):
        self.accountNum = accountNum
        self.owner = owner
        self.balance = 0.0
        User.allUsersAccount.append( self )

    def make_withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            #print(f"New balance: {self.balance}")
        else:
            print( "We cannot process your withdrawal." )
            print( f"You currently have {self.balance}." )
            print( f"And you are trying to withdraw {amount}." )
        return self

    def display_User_Balance(self):
        print( f"User Name: {self.owner}, Balance: ${self.balance}." )
        return self

    def deposit( self, amount ):
        self.balance += amount
        return self

    def validateFunds(self, amount):
        if self.balance > amount:
            return True
        else:
            return False
        return self

    def transfer_Money(self, owner, amount):
        if self.validateFunds(amount):
            self.make_withdrawal( amount )
            owner.deposit( amount )
        else:
            print( "You don't have enough funds to transfer." )
        return self


