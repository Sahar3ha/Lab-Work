#Write a Python program to sum all the items in a list.
total=0
list=[1,2,3,4,5,6,7,8]
for i in range(0,len(list)):
    total=total+list[i]
print(f"Sum of the elements is:",total)    