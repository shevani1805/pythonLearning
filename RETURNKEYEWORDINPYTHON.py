s_username="EMC"
s_password="345"

username=input("Enter value for username:")
password=input("Enter value for password:")

def validate():
    if(s_username== uname and s_password==password):
        return correct
    else:
        return wrong 
        
a=validate()       
print(a)