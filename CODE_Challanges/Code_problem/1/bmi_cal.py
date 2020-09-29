#Adult Body Mass Index Calculator

weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in meter:"))

BMI=((weight/height)/height)

print("your BMI is:",BMI)


##################


def bmi(weight,height):
    BMI = (weight/(height*height))
    print("BMI = ",BMI) 

bmi(float(input("Enter your weight in kg:")), float(input("Enter your height in meter:")))

