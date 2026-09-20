#Create a program to check eligibility of a person to get car license.
age=int(input('Enter your Age: '))
if 7 < age < 18:
    print('You are not eligible to get car licence!')
elif age==18:
    print('You are eligible to get licence but you hae to come physically with your identity card like Aadhaar for passing the test!')
elif 18 < age < 101:
    print('You are eligible to get car licence!')
else:
    print('It is not a logical age')