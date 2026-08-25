A1=int(input("enter the first number:"))
A2=int(input("enter the second number:"))
A3=int(input("enter the third number:"))

sum=A1+A2+A3
if(sum==180):
    print(f'{sum} is a valid triangle') 

else:
    print(f'{sum} is not a valid triangle')