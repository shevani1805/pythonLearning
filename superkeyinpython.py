class A ():
    def display(self):
        print(A)

    def display(self):
        print("i am in class A")

class B ():
    def display(self):
        print("you are i n class B")
        print(B)

class C (B,A):
    def __init__(self):
        super().__init__()
        print("C")
    def display (self):
        print("you are in class C")    

ob1=C()

