# the number of minutes that is passed since midnight 
NoOfMinutes = int(input("Enter the minutes passed since midnight: "))
Hours = (NoOfMinutes // 60)
Minutes = (NoOfMinutes % 60)
print(f"the hours is {Hours} ")
print(f"the minutes is {Minutes}")
print(f"{Hours}:{Minutes}")