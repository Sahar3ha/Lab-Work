#Check whether the user input number is even or odd and display it to user.
user_number = int(input("Enter your number : "))
if (user_number%2) == 0 :
    print("{0} is even".format(user_number))
else  :
    print("{0} is odd".format(user_number))