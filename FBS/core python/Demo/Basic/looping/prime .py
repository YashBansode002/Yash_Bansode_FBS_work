

# n = int (input('enter number:'))


# for num in range (2,n+1):
#     for i in range(2,num):
#         if (num % i == 0 ):
#               break   
#     else:
#         print(num,end=',')


n=int(input('enter n '))
num = 2
while n>0:
    for i in range(2,num):
        if num%i==0:
            break
    else :
        print(num)
        n-=1
    num+=1