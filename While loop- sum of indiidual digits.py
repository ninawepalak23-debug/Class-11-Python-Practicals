n=int(input("Enter an integer: "))
s=0
i=0
l=len(str(n))
while i>=0 and i<l:
    digit=n%10
    s=s+digit
    n=n//10
    i=i+1
print("Sum of indiidual digits is: ",s)
