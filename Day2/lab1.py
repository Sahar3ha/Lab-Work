# convert seconds into day hour minute
sec = int(input("Enter seconds : "))
day = sec/(60*60*24)
hours = sec/(60*60)
minutes = sec/(60)
print("The following day is {}" .format(day))
print("The following hours is {}" .format(hours))
print("The following minutes is {}" .format(minutes))