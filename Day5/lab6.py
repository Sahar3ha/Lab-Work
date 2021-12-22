#Write a Python program to count the number of even and odd numbers from a series of numbers.
list = [1,2,3,4,5,6,7,8,9,10]
count_odd = 0
count_even = 0
for x in list:
    if not x % 2:
        count_even+=1
    else:
        count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)