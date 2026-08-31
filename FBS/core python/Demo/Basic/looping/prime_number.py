num=int(input('enter the number:'))

for i in range(2,num):
    if (num % i == 0):
        print(f'{num} is not primr number:')
        break

else:
      print(f'{num}is a prime number ')