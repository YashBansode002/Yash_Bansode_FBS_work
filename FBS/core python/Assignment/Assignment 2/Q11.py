amount=int(input('enter the amount:'))


n2000=amount//2000
amount=amount%2000

n500=amount//500
amount=amount%500

n200=amount//200
amount=amount%200

n100=amount//100
amount=amount%100

n50=amount//50
amount=amount%50

n20=amount//20
amount=amount%20

n10=amount//10
amount=amount%10

n5=amount//5
amount=amount%5

n2=amount//2
amount=amount%2

n1=amount//1
amount=amount%1
print(f"2000 notes:",n2000)


print(f"500 notes:",n500)
print(f"200 notes:",n200)
print(f"100 notes:",n100)
print(f"50 notes:",n50)
print(f"20 notes:",n20)
print(f"10 notes:",n10)
print(f"n5 notes:",n5)
print(f"n2 notes:",n2)
print(f"n1 notes:",n1)