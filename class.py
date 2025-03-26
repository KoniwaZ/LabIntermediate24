class CashRegister:

    def __init__(self):
        self.total = 0
        self.count = 0

    def addItem(self, price):
        self.count = self.count + 1
        self.total = self.total + price

    def getTotal(self):
        return self.total

    def getCount(self):
        return self.count

    def clear(self):
        self.total = 0
        self.count = 0


cash = CashRegister()
cash.addItem(10000)
print(cash.getCount())
print(cash.getTotal())
cash.clear()
print(cash.getCount())
print(cash.getTotal())
