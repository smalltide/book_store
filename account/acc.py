class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(self.filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """This class generates checking account objects"""

    type = "Checking"

    def __init__(self, filepath, fee):
        #Account.__init__(self,filepath)
        #super(Checking, self).__init__(filepath)
        super().__init__(filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee


checking = Checking("account/balance.txt", 1)
checking.transfer(100)
print(checking.type)
print(checking.balance)
checking.commit()

checking2 = Checking("account/balance.txt", 1)
checking2.transfer(100)
print(checking.type)
print(checking2.balance)
print(checking2.__doc__)
checking2.commit()
