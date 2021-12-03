#
NoOfMinutes = int(input("enter the minutes oassed since midnight: "))
Hours = (NoOfMinutes // 60)
Minutes = (NoOfMinutes % 60)
print(f"the hours is {Hours} ")
print(f"the minutes is {Minutes}")
print(f"{Hours} :{Minutes}")