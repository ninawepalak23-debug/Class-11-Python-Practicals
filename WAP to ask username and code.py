a=input("Enter your username: ")
b=input("Enter your code: ")
while a in b:
    print("Your code should not contain your username.")
    print("Please try again")
    b = input("Enter your code: ")
else:
    print("Your code is valid..")
    print("Your username is", a)
    print("Your code is ",b)
