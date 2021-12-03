#find BMI of a person where take mass and height as input from the user
mass = int(input("Enter mass of person in kg :"))
height = int(input("Enter height of person in meter :"))
BMI = (mass/(height*height))
print(f"the BMI value of a person is {BMI}")