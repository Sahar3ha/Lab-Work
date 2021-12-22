#Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
if (a==b==c)or (a==b) or (a==c) or (b==a) or (b==c) or (c==a) or (c==b):
    print("the sum is zero")
else :
    sum = a+b+c
    print("the sum of three integers is :",sum)