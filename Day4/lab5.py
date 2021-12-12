#A student will not be allowed to sit in exam if his/her attendence is less than 75%.Take following input from user Number of classes held Number of classes attended.And print percentage of class attended Is student is allowed to sit in exam or not.
a = int(input("Number of classes held : "))
b = int(input("Number of classes attended : "))

percentage = int((b/a)*100)
print(f"The Percentage is: ", percentage, "%")
if percentage <=75 :
    print("You are not allowed to sit in the exam")
elif(percentage >=75):
    print("you are allowed to sit in the exam")
