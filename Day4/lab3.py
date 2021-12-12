#
age = int(input("Enter your age :"))

gender = (input("Enter you gender : "))

if (gender == "female") :
    print("your are assigned to urban areas")
elif (gender == "male"):
    if ( age>=20 and age<=40):
        print("you may work anywhere u want")
    elif( age >=40 and age<60):
        print("you are assigned to urban areas")
if (age <20 or age >60):
    print("ERROR")