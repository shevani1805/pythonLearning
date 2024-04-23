class laptop():
    chargertype="C TYPE"

    def __init__(self):
        self.brand=34
        self.price=""

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

hp=laptop()
hp.setprice(20000)
hp.getprice()                
