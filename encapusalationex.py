class company():
    def __init__(self):
        self.__companyName="google"

    def companyName (self):
        print(self.__companyName)    

c1=company()
c1.companyName()
print(c1._companyName)        