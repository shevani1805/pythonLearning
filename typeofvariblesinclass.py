class phone ():
    def __init__(self,brand,price,chargertype):
        self.brand=brand 
        self.price=price
        self.chargertype= chargertype
    def display (self):
        print("brand:",self.brand)    
        print("price:",self.price)
        print("chargertype",self.chargertype)

samsung=phone("samsung","1000","B-type")
samsung.display()

redmi= phone("redmi","5000","C-type")
redmi.display()