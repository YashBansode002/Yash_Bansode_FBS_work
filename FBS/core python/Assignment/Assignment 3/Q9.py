Math=int(input("enter the marks of math:"))
physics=int(input("enter the marks of physics:"))
chemistry=int(input("enter the marks of chemistry:"))
history=int(input("enter the marks of history:"))
biology=int(input("enter the marks of biology:"))
total_marks=Math+physics+chemistry+history+biology
percentage=(total_marks/500)*100
if(percentage>=90):
    print(f'{percentage}% is first class with distinction')
elif(percentage>=80):
    print(f'{percentage}% is second class without distinction')  
else:
    print(f'{percentage} is third  class')