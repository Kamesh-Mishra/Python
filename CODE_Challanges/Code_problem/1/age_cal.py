#Age Calculator

"""
Problem Statement:
    Lets assume your present age is 21 today
    What would be your age after 5 years from today 
    How old were you 10 years back

"""


age = int(input("Enter the present age:"))

age_after_5_years = (age+5)
print("age after 5 years from today is:",age_after_5_years)

age_10_years_back = (age-10)
print("age 10 years back from today is:",age_10_years_back)


#####################################



def age_cal(age):
    print('age after 5 years from today is',age+5)
    print('age 10 years back from today is',age-10)
    
age_cal(int(input("enter present age : ")))




###########################################