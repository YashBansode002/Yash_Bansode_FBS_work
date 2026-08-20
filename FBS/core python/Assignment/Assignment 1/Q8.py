days=int(input('total number of the days :'))

#calculated 
year=days//365
day2=days%365
weak=day2//7
day3=day2%7

print(f'the convertion is {year}year,{weak}weak,{day3}days')







