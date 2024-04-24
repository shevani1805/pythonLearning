class employee():
    def __init__ (self,name,salary):
        self.name=name
        self.salary=salary

class manger(employee):
    def __init__(self,department):
        self.department=department        

    def display (self):
        print(self.name,self.salarey,self.department)  

m1=manger("cse")
m1.display()          