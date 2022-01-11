#Given a n digit number. FInd the sum of its digit:

number = int(input("Enter a number "))
sumofdigits = 0
for digit in len(number):
    sumofdigits += int(digit)
print(sumofdigits)    