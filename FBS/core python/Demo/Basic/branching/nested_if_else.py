gender = input('enter the gender(M/F):')
age = int(input('enter the age:'))

if(gender == 'F'):
    if(age>=18):
        print('girl is eligible for marriage')
    else:
        print('padhai karlo')
else:
    if(age>=21):
        print('boy is eligible for marriage')
    else:
        print('kama lo')

