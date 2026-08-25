
ticket_price=int(input("enter the ticket price:"))
total=0
for i in range(5):
    age=int(input("enter the age:"))
    if(age<12):
        amount=ticket_price-(ticket_price*30/100)

        print(f'ticket price is {amount}')
        total = total +amount
    elif(age>59):
        amount=ticket_price-(ticket_price*50/100)
        print(f'ticket price is {amount}')
        total = total +amount
    else:
        amount=ticket_price
        total = total +amount
        print(f'ticket price is {ticket_price}')

print(total)