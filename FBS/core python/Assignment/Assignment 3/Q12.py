num =int (input("enter the number:"))
orignal=num
reverse=0
while(num > 0):
    d = num%10
    reverse=reverse*10+d    
    num = num//10
if(orignal==reverse):
    print(f'the number is palindrome')  
else:
    print(f'the number is not palindrome')

