n=int(input("Enter the number of inputs you want to compare: "))
num=int(input("Enter the number: "))
g=num
i=1
while i<n:
    num=int(input("Enter the number: "))
    if num>g:
        g=num
    i=i+1
print("The Greatest number is:",g)