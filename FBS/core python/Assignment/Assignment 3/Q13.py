unit=int(input("enter the unit consumed:"))

if unit<=50:
    bill=unit*0.5
    
elif  unit<=150:
    bill=(50*0.5)+((unit-50)*0.75)
   
elif unit<=250:
    bill=(150*0.75)+(100*0.75)+((unit-150)*1.20)
    
else:
    bill=(50*0.5)+(100*0.75)+(100*1.20)+((unit-250)*1.50)

    

surcharge=bill*20/100
total=bill+surcharge
print(f'the bill is {bill}')
print(f'the surcharge is {surcharge}')
print(f'the total bill is {total}')
