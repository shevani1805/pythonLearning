a=[]
print("Enter 10 numbers:")
for i in range (5): 
    num=int(input("Enter num "+str(i+1)))
    a.append(num)
print(a)
 
sum=0
for i in a:
    sum=sum+i
print(sum)     