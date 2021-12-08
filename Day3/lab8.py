#
for i in range(3) :
   user_input = input("Enter your name : ")
   password = input("Enter your password : ")
   
   if (user_input == "Saharsha" ) and (password == "123"):
      print("Logged in successful")
      break
   else :
      print("Invalid credentials")
else:
   print("Attemt finished")

