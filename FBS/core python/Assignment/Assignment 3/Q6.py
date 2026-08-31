cp=int(input("enter the cost price:"))
sp=int(input("enter the selling price:"))
if(sp>cp):
    profit=sp-cp
    profit_percentage=(profit/cp)*100
    print(f'profit is {profit}')
    print(f'profit percentage is {profit_percentage}')
elif(cp>sp):
    loss=cp-sp
    loss_percentage=(loss/cp)*100
    print(f'loss is {loss}')
else:
    print("no profit, no loss")