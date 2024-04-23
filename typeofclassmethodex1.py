class laptop():
    chargertype="C TYPE"

    def __init__(self):
        self.brand=34
        self.price=""

    def setprice(self,price):
        self.price=price

    def getprice(self):
        print(self.price)

    def changechargertype(cls):
        cls.chargertype="b type"
        print("charger type changed to B")
hp=laptop()
hp.setprice(20000)
hp.getprice()        

laptop.changechargertype()
