class laptop:
    def __init__(self):
        self.price=0
        self.processor=""
        self.ram=""
    def display(self):
        print("display")    

hp=laptop()
hp.price=50000
hp.ram=""
print(hp.price)