F=int(input('Feet'))
I=int(input('Inch:'))

TC=(F*30.48)+(I*2.54) 

M=TC/100

print(f'Meter:{M},Centimeter:{TC}')