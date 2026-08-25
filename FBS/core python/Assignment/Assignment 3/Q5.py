A=int(input("enter the first angle:"))
B=int(input("enter the second angle:"))
C=int(input("enter the third angle:"))  

if(A==B and B==C and A==C):
    print(f'{A},{B},{C} is a equilateral triangle')
elif(A==B or B==C or A==C):
    print(f'{A},{B},{C} is a isosceles triangle')
else:
    print(f'{A},{B},{C} is a scalene triangle')