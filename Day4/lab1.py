#Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else.print ‘COMMON YEAR’.
year = int(input("Enter a year : "))
if (year%4 == 0 and year%100 !=0 or year %400 == 0):
    print('LEAP YEAR')
else:
    print('COMMON YEAR')
