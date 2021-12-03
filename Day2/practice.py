# #
class_a = int(input("Enter number of students in class a: "))#20
class_b = int(input("Enter number of students in class b: "))#21
class_c = int(input("Enter number of students in class c: "))#22

#print("Total desk: ",a+b+c)

a=0
b=0
c=0


if(class_a%2!=0):
    a=(class_a//2)+1
else:
    a=class_a/2
print("A",a)


if(class_b%2!=0):
    b=(class_b//2)+1
else:
    b=class_b/2
print("B",b)

if(class_c%2!=0):
    c=(class_c//2)+1
else:
    c=class_c/2
print("C",c)

# if(a<b and a<c):
#     print("Class A requires: ",a)
# elif(b<a and b<c):
#     print("Class B requires: ",b)
# elif(c<a and c<b):
#     print("Class C requires: ",c )

# eachdesk = ((a+b+c)//2)
# print(f"The smallest number of desk possible to be purchased is {eachdesk}")

