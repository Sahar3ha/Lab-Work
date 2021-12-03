#
class_a = int(input("Enter number of students in class a : "))
class_b = int(input("Enter number of students in class b : "))
class_c = int(input("Enter number of students in class c : "))
A = class_a//2
if(class_a%2 !=0):
    A = (class_a//2)+1
elif(class_a%2 ==0) :
    A = (class_a//2)
B = class_b//2
if(class_b%2 !=0):
    B = (class_b//2)+1
elif (class_b%2 ==0):
    B = (class_b//2)
C = class_c//2
if(class_c%2 !=0):
    C = (class_c//2)+2
elif (class_c%2 ==0):
    C = (class_c//2)
print(f"The smallest number required is {A+B+C}")

