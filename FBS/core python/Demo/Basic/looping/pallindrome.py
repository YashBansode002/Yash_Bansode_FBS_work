num=int(input('enter the number: '))
org=num
rev=0

while (num>0):
    d=num%10
    num=num//10
    rev=rev*10+d

if(org==rev):
    print(f'{org}:is palindrome number')
else:
    print (f'{org}:is not pallindrome')