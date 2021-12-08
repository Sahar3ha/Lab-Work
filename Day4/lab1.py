#
user = int(input("Enter a year : "))
if (user%4 == 0):
    print('LEAP YEAR')
elif (user%100 != 0):
    print('COMMON YEAR')
