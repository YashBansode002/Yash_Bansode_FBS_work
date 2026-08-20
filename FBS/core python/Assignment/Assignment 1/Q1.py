#take input 
p=float(input("Physics:"))
c=float(input('Chemestry:'))
m=float(input('Math:'))
b=float(input('Biology:'))
h=float(input('History:'))

#perform Addition of the subject

sum=p+c+m+b+h

#calculate persentage
total_mark=500
mark_obtain=sum

#formula
persentage = mark_obtain / total_mark *100

print(f'The persentage obtain :',persentage)