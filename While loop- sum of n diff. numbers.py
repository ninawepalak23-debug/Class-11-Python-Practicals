n=int(input("Enter how many numbers' sum you want to calculate: "))
sum=0
i=0
while i<n:
    num=int(input("Enter a number: "))
    sum=sum+num
    i=i+1
print("Sum of these numbers is: ",sum)