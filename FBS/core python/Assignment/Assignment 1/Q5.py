#take the input 
P=int(input('enter the principle amount P:'))
T=int(input('enter the time T:'))
R=int(input('enter rate of the intrest R:'))
#perform calculation 

CI= P * (1+R/100)**T - P

#calculate 



print(f'the coumpound intrest is :',CI)