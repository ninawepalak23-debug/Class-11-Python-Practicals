'''input a number from user. Then ask for Boolean value(0 or 1).
If user input 1, then print increasing star pattern.
if user input 0, then print decreasing star pattern.'''
n=int(input("Enter a number: "))
print("0 is for False and 1 is for True")
p=int(input("Enter a number 0 or 1: "))
if p==1:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()

elif p==0:
    for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print()

else:
    print("Invalid input! Please try again.")