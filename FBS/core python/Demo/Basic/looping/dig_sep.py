num =int (input("enter the number:"))
sum=0
while(num > 0):
    d = num%10
    print(d)
    sum+=d
    num = num//10
print(f'the addition :',sum)
