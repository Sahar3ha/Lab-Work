#
subject_1 = float(input("Enter your marks : "))
subject_2 = float(input("Enter your marks : "))
subject_3 = float(input("Enter your marks : "))
subject_4 = float(input("Enter your marks : "))

total,average,percentage,grade = None, None, None, None

total = subject_1+subject_2+subject_3+subject_4
average = total/4.0
percentage = (total/400.0)*100 
if average>=70:
    Grade = "A"
elif average>=60 and average <90:
    Grade = "B"
elif average>=40 and average <80:
    Grade = "C"
elif average>=40 and average <70:
    Grade = "D"
else :
        Grade = "F"
print (f"The Total marks is:   ", total, "/ 500.00")
print (f"The Average marks is: ", average)
print (f"The Percentage is:    ", percentage, "%")
print (f"The Grade is:         ", grade)
