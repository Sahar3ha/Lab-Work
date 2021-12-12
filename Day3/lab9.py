#Given a n digit number. FInd the sum of its digit:

number = int(input("Enter a number "))
sumofdigits = 0
for digit in str(number):
    sumofdigits += int(digit)
print(sumofdigits)    