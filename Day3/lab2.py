#
subject_1 = int(input("Enter your marks : "))
subject_2 = int(input("Enter your marks : "))
subject_3 = int(input("Enter your marks : "))
subject_4 = int(input("Enter your marks : "))


total = subject_1+subject_2+subject_3+subject_4
average = total/4
percentage = (total/400)*100 
if average>=70:
    grade = "A"
elif average>=60 and average <90:
    grade = "B"
elif average>=40 and average <80:
    grade = "C"
elif average>=40 and average <70:
    grade = "D"
else :
        Grade = "F"
print (f"The Total marks is:   ", total, "/ 400")
print (f"The Average marks is: ", average)
print (f"The Percentage is:    ", percentage, "%")
print (f"The Grade is:         ", grade)
