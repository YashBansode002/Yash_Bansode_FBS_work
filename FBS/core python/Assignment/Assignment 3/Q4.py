#angle 
A=int(input("enter the first angle:"))
B=int(input("enter the second angle:"))    
C=int(input("enter the third angle:"))    

if( A+B>C and B+C>A and A+C>B):
    print(f'{A},{B},{C} is a valid triangle')
else:
    print(f'{A},{B},{C} is not a valid triangle')
